import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Create window
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Snake")

# =========================
# Snake class
# =========================
class Snake:
    def __init__(self):
        self.size = 20
        self.body = [(300, 200)]  # list of segments
        self.dx = self.size
        self.dy = 0
        self.grow = False  # growth flag

    def move(self):
        head_x, head_y = self.body[0]

        # Create new head based on direction
        new_head = (head_x + self.dx, head_y + self.dy)
        self.body.insert(0, new_head)

        # Remove tail unless growing
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(
                screen,
                (0, 200, 0),
                (segment[0], segment[1], self.size, self.size)
            )

    def change_direction(self, dx, dy):
        # Prevent reversing
        if self.dx == -dx and self.dy == -dy:
            return
        self.dx = dx
        self.dy = dy


# =========================
# Food generation
# =========================
def generate_food(snake, WIDTH, HEIGHT, size):
    while True:
        x = random.randint(0, (WIDTH // size) - 1) * size
        y = random.randint(0, (HEIGHT // size) - 1) * size

        # Avoid spawning inside snake
        if (x, y) not in snake.body:
            return (x, y)


# =========================
# Config
# =========================
clock = pygame.time.Clock()

LEVEL_FPS = {
    1: 20,
    2: 25,
    3: 30
}

LEVEL_COLORS = {
    1: (255, 255, 255),   # white
    2: (255, 215, 0),     # gold
    3: (0, 183, 235)      # light blue
}

FOOD_LIFETIME = 5000  # 5 seconds

# =========================
# Init game objects
# =========================
snake = Snake()
food_pos = generate_food(snake, WIDTH, HEIGHT, snake.size)
food_spawn_time = pygame.time.get_ticks()

SCORE = 0
LEVEL = 1

# Fonts
font_small = pygame.font.SysFont("Georgia", 20)
font_big = pygame.font.SysFont(None, 50)

game_over_text = font_big.render("Game Over!", True, (255, 255, 255))

# =========================
# Game loop
# =========================
running = True
game_over = False

while running:
    # ---------------------
    # Events
    # ---------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(0, -snake.size)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(0, snake.size)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(-snake.size, 0)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(snake.size, 0)

    # ---------------------
    # Game logic
    # ---------------------
    if not game_over:
        snake.move()

        head = snake.body[0]
        head_x, head_y = head

        # Wall collision
        if (head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT):
            game_over = True

        # Self collision
        if head in snake.body[1:]:
            game_over = True

        # Food eaten
        if head == food_pos:
            snake.grow = True
            food_pos = generate_food(snake, WIDTH, HEIGHT, snake.size)
            food_spawn_time = pygame.time.get_ticks()

            SCORE += random.randint(1, 3)

        # Food expiration
        current_time = pygame.time.get_ticks()
        if current_time - food_spawn_time > FOOD_LIFETIME:
            food_pos = generate_food(snake, WIDTH, HEIGHT, snake.size)
            food_spawn_time = current_time

        # Level update
        if SCORE >= 10:
            LEVEL = 3
        elif SCORE >= 5:
            LEVEL = 2
        else:
            LEVEL = 1

    # ---------------------
    # Rendering
    # ---------------------
    if not game_over:
        screen.fill(LEVEL_COLORS.get(LEVEL, (255, 255, 255)))

        snake.draw(screen)

        # Food color warning (last 1 sec)
        current_time = pygame.time.get_ticks()
        time_left = FOOD_LIFETIME - (current_time - food_spawn_time)

        if time_left < 1000:
            food_color = (255, 100, 100)
        else:
            food_color = (200, 0, 0)

        pygame.draw.rect(
            screen,
            food_color,
            (food_pos[0], food_pos[1], snake.size, snake.size)
        )

        # UI
        score_text = font_small.render(f"Score: {SCORE}", True, (0, 0, 0))
        level_text = font_small.render(f"Level: {LEVEL}", True, (0, 0, 0))

        screen.blit(score_text, (5, 5))
        screen.blit(level_text, (5, 25))

    else:
        screen.fill((200, 0, 0))

        screen.blit(game_over_text, (WIDTH//2 - 120, HEIGHT//2 - 50))

        score_display = font_big.render(f"Score: {SCORE}", True, (255, 255, 255))
        level_display = font_big.render(f"Level: {LEVEL}", True, (255, 255, 255))

        screen.blit(score_display, (180, 200))
        screen.blit(level_display, (180, 250))
    # ---------------------
    # Update
    # ---------------------
    pygame.display.flip()
    clock.tick(LEVEL_FPS.get(LEVEL, 20))