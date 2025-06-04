import pygame
import sys
import random

# === Constants ===
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# === Game setup ===
pygame.init()
font = pygame.font.SysFont(None, 50)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smart Pong")
clock = pygame.time.Clock()

# === Game objects ===
paddle_width, paddle_height = 10, 100
player = pygame.Rect(50, 250, paddle_width, paddle_height)
cpu = pygame.Rect(740, 250, paddle_width, paddle_height)
ball = pygame.Rect(390, 290, 20, 20)
ball_speed = [4, 4]
paddle_speed = 6

# === Game state and scoring ===
player_score = 0
cpu_score = 0
game_state = "start"

# === Initial CPU difficulty ===
base_cpu_focus = random.uniform(0.5, 0.7)  # Random starting difficulty
cpu_focus = base_cpu_focus

# === Helper: Reset ball to center ===
def ball_reset():
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ball_speed[0] *= -1

# === Game loop ===
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game_state == "start" and event.key == pygame.K_SPACE:
                game_state = "play"
            elif game_state == "game_over" and event.key == pygame.K_r:
                # Restart game
                player_score = 0
                cpu_score = 0
                ball_reset()
                base_cpu_focus = random.uniform(0.5, 0.7)
                cpu_focus = base_cpu_focus
                game_state = "start"

    # === Gameplay logic ===
    if game_state == "play":
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player.top > 0:
            player.y -= paddle_speed
        if keys[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
            player.y += paddle_speed

        # CPU movement with adaptive logic
        score_diff = cpu_score - player_score
        cpu_focus = base_cpu_focus - (score_diff * 0.1)
        cpu_focus = max(0.2, min(cpu_focus, base_cpu_focus))  # Clamp to never exceed starting level

        if random.random() < cpu_focus:
            target_y = ball.centery + random.randint(-20, 20)
            if cpu.centery < target_y and cpu.bottom < SCREEN_HEIGHT:
                cpu.y += paddle_speed
            elif cpu.centery > target_y and cpu.top > 0:
                cpu.y -= paddle_speed

        # Ball movement
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Bounce off top and bottom walls
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_speed[1] = -ball_speed[1]

        # Bounce off paddles
        if ball.colliderect(player) or ball.colliderect(cpu):
            ball_speed[0] = -ball_speed[0]

        # Scoring
        if ball.left <= 0:
            cpu_score += 1
            ball_reset()
        elif ball.right >= SCREEN_WIDTH:
            player_score += 1
            ball_reset()

        # Win condition
        if player_score == 5 or cpu_score == 5:
            game_state = "game_over"

    # === Drawing ===
    screen.fill(BLACK)

    if game_state == "start":
        title = font.render("ADAPTIVE PONG", True, WHITE)
        prompt = font.render("Press SPACE to start", True, WHITE)
        instructions = font.render("Use W and S keys to control your paddle", True, WHITE)
        instructions_2 = font.render("First to 5 points wins!", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 200))
        screen.blit(prompt, (SCREEN_WIDTH // 2 - prompt.get_width() // 2, 300))
        screen.blit(instructions, (SCREEN_WIDTH // 2 - instructions.get_width() // 2, 360))
        screen.blit(instructions_2, (SCREEN_WIDTH // 2 - instructions_2.get_width() // 2, 400))

    elif game_state == "play":
        # Draw paddles, ball, and center line
        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.rect(screen, WHITE, cpu)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

        # Draw scores
        player_text = font.render(str(player_score), True, WHITE)
        cpu_text = font.render(str(cpu_score), True, WHITE)
        screen.blit(player_text, (300, 50))
        screen.blit(cpu_text, (480, 50))

    elif game_state == "game_over":
        winner = "You win!" if player_score == 5 else "CPU wins!"
        win_text = font.render(winner, True, WHITE)
        restart_text = font.render("Press R to restart", True, WHITE)
        screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, 200))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 300))

    pygame.display.flip()
    clock.tick(FPS)
