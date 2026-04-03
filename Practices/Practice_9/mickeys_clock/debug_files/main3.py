import pygame
import sys
import datetime

pygame.init()

# --- Screen setup ---
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

# --- Load images ---
background = pygame.image.load("images/background.png").convert_alpha()
righthand_big = pygame.image.load("images/righthand3.png").convert_alpha()
lefthand_big = pygame.image.load("images/lefthand.png").convert_alpha()

# --- Scale hands ---
righthand = pygame.transform.smoothscale(righthand_big, (100, 200))
lefthand = pygame.transform.smoothscale(lefthand_big, (100, 200))

# --- FIXED CLOCK CENTER ---
CENTER = [284, 240]

# --- ANCHOR POINT INSIDE IMAGE (wrist position) ---
RIGHT_HAND_OFFSET = [righthand.get_width() // 2 - 150, righthand.get_height()]
LEFT_HAND_OFFSET  = [lefthand.get_width() // 2, lefthand.get_height()]


def blit_rotate_anchor(surface, image, anchor_pos, anchor_offset, angle):
    rotated_image = pygame.transform.rotate(image, angle)

    anchor_vector = pygame.math.Vector2(anchor_offset)
    rotated_vector = anchor_vector.rotate(-angle)

    rect = rotated_image.get_rect(center=(
        anchor_pos[0] - rotated_vector.x,
        anchor_pos[1] - rotated_vector.y
    ))

    surface.blit(rotated_image, rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                CENTER[0] -= 2   # move left
            elif event.key == pygame.K_l:
                CENTER[0] += 2   # move right
            elif event.key == pygame.K_i:
                CENTER[1] -= 2   # move up
            elif event.key == pygame.K_k:
                CENTER[1] += 2   # move down

            print("CENTER:", CENTER)

    # --- Time ---
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    # --- Angles ---
    angle_minutes = -6 * minutes - 0.1 * seconds
    angle_seconds = -6 * seconds

    # --- Draw ---
    screen.blit(background, (0, 0))

    # DEBUG: center point
    pygame.draw.circle(screen, (255, 0, 0), CENTER, 5)

    # --- Draw hands ---
    blit_rotate_anchor(screen, righthand, CENTER, RIGHT_HAND_OFFSET, angle_minutes)
    blit_rotate_anchor(screen, lefthand, CENTER, LEFT_HAND_OFFSET, angle_seconds)
    pygame.display.update()
    clock.tick(60)