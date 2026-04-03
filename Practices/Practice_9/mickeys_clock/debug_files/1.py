import pygame
import sys
import os
import datetime

pygame.init()

# --- Settings ---
WIDTH, HEIGHT = 800, 600
CENTER = (WIDTH // 2, HEIGHT // 2)  # true clock center
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

# --- Load images ---
BASE_PATH = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(BASE_PATH,'images','background.png')).convert_alpha()
right_hand = pygame.image.load(os.path.join(BASE_PATH,'images','righthand.png')).convert_alpha()
left_hand = pygame.image.load(os.path.join(BASE_PATH,'images','lefthand.png')).convert_alpha()

# --- Offsets from center (from check scripts) ---
offset_rx, offset_ry = 83, -59
offset_lx, offset_ly = -75, -46

# --- Compute background top-left to center it ---
bg_rect = background.get_rect()
bg_topleft = (CENTER[0] - bg_rect.width // 2 + 23,  # +23 to match your manual shift
              CENTER[1] - bg_rect.height // 2)

# --- blitRotate helper ---
def blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0]-originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)

# --- Main loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    # --- Draw background centered ---
    screen.blit(background, bg_topleft)

    # --- Get current time ---
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    # --- Calculate angles for hands ---
    # negative to rotate clockwise
    minute_angle = -(minutes + seconds / 60) * 6  # 360 / 60
    second_angle = -seconds * 6

    # --- Draw hands with offsets ---
    right_origin = (right_hand.get_width()//2, right_hand.get_height()//2)
    left_origin = (left_hand.get_width()//2, left_hand.get_height()//2)

    blitRotate(screen, right_hand,
               (CENTER[0] + offset_rx, CENTER[1] + offset_ry),
               right_origin,
               second_angle)

    blitRotate(screen, left_hand,
               (CENTER[0] + offset_lx, CENTER[1] + offset_ly),
               left_origin,
               minute_angle)

    # --- Optional debug: pivot red dot ---
    pygame.draw.circle(screen, (255,0,0), CENTER, 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()