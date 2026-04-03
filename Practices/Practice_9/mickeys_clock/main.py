import pygame
import sys
import datetime

pygame.init()

# --- Screen setup ---
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# --- Load images ---
background = pygame.image.load("images/background.png").convert_alpha()
righthand_big_img = pygame.image.load("images/righthand3.png").convert_alpha()
lefthand = pygame.image.load("images/lefthand.png").convert_alpha()

righthand = pygame.transform.scale(righthand_big_img, (100, 200))
# --- Hand offsets to match center ---
center_x, center_y = WIDTH // 2, HEIGHT // 2

# offsets (MUST ALIGN):
# R: [-40, 95]
# L: [-25, 80]

# Optional: tweak offsets if hand images pivot isn't centered
# offset_r = [-60, -90]  
# offset_l = [-70, -95]

# --- Clock center ---
center = (WIDTH // 2, HEIGHT // 2)

# --- Pivot points (bottom-center of each hand) ---
pivot_r = [righthand.get_width() // 2, righthand.get_height()]
# pivot_r = [-40, 95]
pivot_l = [lefthand.get_width() // 2, lefthand.get_height()]
# pivot_l = [-25, 100]

offset_r = [0, 0]
offset_l = [0, 0]

# bg offset
bg_offset = [-30, 5]

def blit_rotate(surface, image, center, pivot, angle):
    """Rotate image around pivot and draw it"""
    # Rotate image
    rotated_image = pygame.transform.rotate(image, angle)

    # Pivot vector
    pivot_vector = pygame.math.Vector2(pivot)

    # Rotate pivot
    rotated_pivot = pivot_vector.rotate(-angle)

    # Get rect so pivot stays at center
    rect = rotated_image.get_rect(
        center=(center[0] - rotated_pivot.x,
                center[1] - rotated_pivot.y)
    )

    # Draw
    surface.blit(rotated_image, rect)


clock = pygame.time.Clock()

# minutes = 0
# seconds = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # --- RIGHT HAND (arrow keys) ---
            if event.key == pygame.K_LEFT:
                offset_r[0] -= 5
            elif event.key == pygame.K_RIGHT:
                offset_r[0] += 5
            elif event.key == pygame.K_UP:
                offset_r[1] -= 5
            elif event.key == pygame.K_DOWN:
                offset_r[1] += 5

            # --- LEFT HAND (WASD) ---
            elif event.key == pygame.K_a:
                offset_l[0] -= 5
            elif event.key == pygame.K_d:
                offset_l[0] += 5
            elif event.key == pygame.K_w:
                offset_l[1] -= 5
            elif event.key == pygame.K_s:
                offset_l[1] += 5
            
            # angle manipulation
            elif event.key == pygame.K_z:
                minutes += 1
            elif event.key == pygame.K_x:
                seconds += 1
            elif event.key == pygame.K_c:
                minutes -= 1
            elif event.key == pygame.K_v:
                seconds -= 1

            # bg offset manipulation
            if event.key == pygame.K_j:
                bg_offset[0] -= 5   # move left
            elif event.key == pygame.K_l:
                bg_offset[0] += 5   # move right
            elif event.key == pygame.K_i:
                bg_offset[1] -= 5   # move up
            elif event.key == pygame.K_k:
                bg_offset[1] += 5   # move down
            print(f"R offset: {offset_r}, L offset: {offset_l}, Minutes: {minutes}, Seconds: {seconds}, bg_offset = {bg_offset}")


    # --- Get current time ---
    now = datetime.datetime.now()
    minutes = now.second
    seconds = now.minute

    # --- Calculate angles ---
    angle_minutes = -6 * minutes - 0.1 * seconds
    angle_seconds = -6 * seconds

    # --- Draw background ---
    screen.blit(background, bg_offset)
    # --- Draw hands ---
    blit_rotate(screen, righthand, center, offset_r, angle_minutes)
    blit_rotate(screen, lefthand, center, offset_l, angle_seconds)
    pygame.display.update()
    clock.tick(60)