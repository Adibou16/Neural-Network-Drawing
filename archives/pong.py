import sys
import random
import pygame


def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_h:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_w:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_h:
        player.bottom = screen_h


def opponent_animation():
    if opponent.top <= ball.y:
        opponent.y += opponent_speed
    if opponent.bottom >= ball.y:
        opponent.y -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_h:
        opponent.bottom = screen_h


def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_w / 2, screen_h / 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))


pygame.init()
clock = pygame.time.Clock()

# Main window setup
screen_w = 1280
screen_h = 960
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Pong')

# Game rectangles
ball = pygame.Rect(screen_w / 2 - 15, screen_h / 2 - 15, 30, 30)
player = pygame.Rect(screen_w - 20, screen_h / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_h / 2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_gray = (200, 200, 200)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed = 7
            if event.key == pygame.K_UP:
                player_speed = -7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_speed = 0

    ball_animation()
    player_animation()
    opponent_animation()

    # Graphics
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_gray, player)
    pygame.draw.rect(screen, light_gray, opponent)
    pygame.draw.ellipse(screen, light_gray, ball)
    pygame.draw.aaline(screen, light_gray, (screen_w / 2, 0), (screen_w / 2, screen_h))

    pygame.display.flip()
    clock.tick(60)
