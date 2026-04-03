import pygame
import sys
import os

pygame.init()

# --- Settings ---
WIDTH, HEIGHT = 800, 600
CENTER = (WIDTH // 2, HEIGHT // 2)  # true clock center

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Right Hand Alignment Checker")
clock = pygame.time.Clock()

# --- Load images ---
BASE_PATH = os.path.dirname(__file__)
try:
    background = pygame.image.load(os.path.join(BASE_PATH,'images','background.png')).convert_alpha()
    right_hand = pygame.image.load(os.path.join(BASE_PATH,'images','righthand.png')).convert_alpha()
    left_hand = pygame.image.load(os.path.join(BASE_PATH, 'images', 'lefthand.png')).convert_alpha()
except:
    print("Error loading images")
    sys.exit()

# --- Adjustable offsets for right hand ---
offset_rx, offset_ry = 83, -59  # tweak these until hand aligns perfectly
offset_lx, offset_ly = -75, -46

# --- Precompute background top-left to center it ---
bg_rect = background.get_rect()
bg_topleft = (CENTER[0] - bg_rect.width // 2 + 23, CENTER[1] - bg_rect.height // 2)

# --- Main loop ---
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Interactive adjustment
            if event.key == pygame.K_LEFT:
                offset_lx -= 1
            elif event.key == pygame.K_RIGHT:
                offset_lx += 1
            elif event.key == pygame.K_UP:
                offset_ly -= 1
            elif event.key == pygame.K_DOWN:
                offset_ly += 1

    screen.fill((0,0,0))

    # --- Draw background centered ---
    screen.blit(background, bg_topleft)
    # screen.blit()
    # --- Draw right hand (plain, no rotation) ---
    right_rect = right_hand.get_rect(center=(CENTER[0] + offset_rx, CENTER[1] + offset_ry))
    screen.blit(right_hand, right_rect)
    left_rect = left_hand.get_rect(center=(CENTER[0] + offset_lx, CENTER[1] + offset_ly))
    screen.blit(left_hand, left_rect)
    # --- Debug overlays ---
    # Pivot red dot = clock center
    pygame.draw.circle(screen, (255,0,0), CENTER, 5)
    # Bounding box of right hand
    pygame.draw.rect(screen, (0,255,0), right_rect, 2)
    pygame.draw.rect(screen, (0,0,255), left_rect, 2)

    # Instructions
    font = pygame.font.SysFont(None, 24)
    text = font.render("Arrow keys = adjust offsets | Red dot = clock center", True, (255,255,255))
    screen.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()