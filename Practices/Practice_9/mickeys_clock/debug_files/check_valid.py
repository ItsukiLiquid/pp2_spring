import pygame
import sys
import os

pygame.init()

# --- Settings ---
WIDTH, HEIGHT = 800, 600
CENTER = (WIDTH // 2, HEIGHT // 2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hand Position Checker")
clock = pygame.time.Clock()

# --- Load images ---
BASE_PATH = os.path.dirname(__file__)
try:
    background = pygame.image.load(os.path.join(BASE_PATH,'images','background.png')).convert_alpha()
    right_hand = pygame.image.load(os.path.join(BASE_PATH,'images','righthand.png')).convert_alpha()
    left_hand = pygame.image.load(os.path.join(BASE_PATH,'images','lefthand.png')).convert_alpha()
except:
    print("Error loading images")
    sys.exit()

# --- Optional offsets to adjust pivot position visually ---
offsets = {
    'right': (-5, 3),  # tweak until hand visually centers
    'left': (0, 0)
}

# --- Main loop ---
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0))

    # draw background
    screen.blit(background, (0,0))

    # draw hands (plain, no rotation)
    right_rect = right_hand.get_rect(center=(CENTER[0]+offsets['right'][0],
                                             CENTER[1]+offsets['right'][1]))
    left_rect = left_hand.get_rect(center=(CENTER[0]+offsets['left'][0],
                                           CENTER[1]+offsets['left'][1]))

    screen.blit(right_hand, right_rect)
    screen.blit(left_hand, left_rect)

    # --- Debug overlays ---
    # pivot red dot
    pygame.draw.circle(screen, (255,0,0), CENTER, 5)
    # bounding boxes
    pygame.draw.rect(screen, (0,255,0), right_rect, 2)
    pygame.draw.rect(screen, (0,255,255), left_rect, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()