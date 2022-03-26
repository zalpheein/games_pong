import pygame, sys

def ball_animation():
    global ball_speed_x, ball_speed_y
    # 실제 볼을 움직임
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # 볼이 플레이 그라운드 안에서 움직이게
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    # 볼이 플레이어와 만났을 때
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('gray12')
light_grey = (200, 200, 200)

# 볼 움직임 속도/스피드
ball_speed_x = 7
ball_speed_y = 7

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball_animation()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    # 중간 세로선
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))


    # Updateing the window
    pygame.display.flip()
    clock.tick(60)
    






















