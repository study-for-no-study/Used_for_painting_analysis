import pygame
import random
import math

# 初始化Pygame
pygame.init()




# 定义颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 设置屏幕尺寸和标题
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

# 定义贪吃蛇和食物
snake = [(200, 200), (210, 200), (220, 200)]
snake_direction = "RIGHT"
turnuri=0
turnrup=0
turnlup=0
turnrdown=0
turnldown=0
turndri=0
turndle=0
turnule=0
snake_speed = 4
food_pos = (random.randint(0, WIDTH // 10 - 1) * 10, random.randint(0, HEIGHT // 10 - 1) * 10)

# 定义函数：绘制贪吃蛇和食物
def draw_snake_and_food():
    screen.fill(WHITE)
    for pos in snake:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], 10, 10))
    pygame.display.update()

# 定义函数：更新贪吃蛇的位置
def move_snake():
    global snake_direction
    global turnuri
    global turnrup
    global turnlup
    global turnrdown
    global turndri
    global turndle
    global turnule
    global turnldown
    if snake_direction == "RIGHT" and turnuri == 0 and turndri == 0:
        snake[2] = (snake[2][0] + 10, snake[2][1])
        snake[1] = (snake[1][0] + 10, snake[1][1])
        snake[0] = (snake[0][0] + 10, snake[0][1])
    elif snake_direction == "RIGHT" and  turnuri == 2:
        snake[2] = (snake[2][0] + 10 , snake[2][1])
        snake[1] = (snake[1][0], snake[1][1] - 10)
        snake[0] = (snake[0][0], snake[0][1] - 10)
        turnuri -= 1
    elif snake_direction == "RIGHT" and  turnuri == 1:
        snake[2] = (snake[2][0] + 10 , snake[2][1])
        snake[1] = (snake[1][0] + 10, snake[1][1])
        snake[0] = (snake[0][0], snake[0][1] - 10)
        turnuri -= 1
    elif snake_direction == "RIGHT" and  turndri == 2:
        snake[2] = (snake[2][0] + 10, snake[2][1])
        snake[1] = (snake[1][0],      snake[1][1] + 10)
        snake[0] = (snake[0][0],      snake[0][1] + 10)
        turndri -= 1
    elif snake_direction == "RIGHT" and  turndri == 1:
        snake[2] = (snake[2][0] + 10, snake[2][1] )
        snake[1] = (snake[1][0] + 10, snake[1][1] )
        snake[0] = (snake[0][0], snake[0][1] + 10)
        turndri -= 1
    elif snake_direction == "LEFT" and turndle == 0 and turnule == 0:
        snake[2] = (snake[2][0] - 10, snake[2][1])
        snake[1] = (snake[1][0] - 10, snake[1][1])
        snake[0] = (snake[0][0] - 10, snake[0][1])
    elif snake_direction == "LEFT" and turndle == 2:
        snake[2] = (snake[2][0] - 10, snake[2][1])
        snake[1] = (snake[1][0], snake[1][1] + 10)
        snake[0] = (snake[0][0], snake[0][1] + 10)
        turndle -= 1
    elif snake_direction == "LEFT" and turndle == 1:
        snake[2] = (snake[2][0] - 10, snake[2][1])
        snake[1] = (snake[1][0] - 10, snake[1][1])
        snake[0] = (snake[0][0], snake[0][1] + 10)
        turndle -= 1
    elif snake_direction == "LEFT" and turnule == 2:
        snake[2] = (snake[2][0] - 10, snake[2][1])
        snake[1] = (snake[1][0], snake[1][1] - 10)
        snake[0] = (snake[0][0], snake[0][1] - 10)
        turnule -= 1
    elif snake_direction == "LEFT" and turnule == 1:
        snake[2] = (snake[2][0] - 10, snake[2][1])
        snake[1] = (snake[1][0] - 10, snake[1][1])
        snake[0] = (snake[0][0], snake[0][1] - 10)
        turnule -= 1
    elif snake_direction == "UP" and turnrup == 0 and turnlup == 0:
        snake[2] = (snake[2][0], snake[2][1] - 10)
        snake[1] = (snake[1][0], snake[1][1] - 10)
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif snake_direction == "UP" and turnrup == 2:
        snake[2] = (snake[2][0], snake[2][1] - 10)
        snake[1] = (snake[1][0] + 10, snake[1][1] )
        snake[0] = (snake[0][0] + 10, snake[0][1] )
        turnrup -= 1
    elif snake_direction == "UP" and turnrup == 1:
        snake[2] = (snake[2][0], snake[2][1] - 10)
        snake[1] = (snake[1][0], snake[1][1] - 10)
        snake[0] = (snake[0][0] + 10, snake[0][1] )
        turnrup -= 1
        
    elif snake_direction == "UP" and turnlup == 2:
        snake[2] = (snake[2][0], snake[2][1] - 10)
        snake[1] = (snake[1][0] - 10, snake[1][1] )
        snake[0] = (snake[0][0] - 10, snake[0][1] )
        turnlup -= 1
    elif snake_direction == "UP" and turnlup == 1:
        snake[2] = (snake[2][0], snake[2][1] - 10)
        snake[1] = (snake[1][0], snake[1][1] - 10)
        snake[0] = (snake[0][0] - 10, snake[0][1] )
        turnlup -= 1   
    elif snake_direction == "DOWN" and turnrdown == 0 and turnldown == 0:
        snake[2] = (snake[2][0], snake[2][1] + 10)
        snake[1] = (snake[1][0], snake[1][1] + 10)
        snake[0] = (snake[0][0], snake[0][1] + 10)
    elif snake_direction == "DOWN" and turnrdown == 2:
        snake[2] = (snake[2][0], snake[2][1] + 10)
        snake[1] = (snake[1][0] + 10, snake[1][1])
        snake[0] = (snake[0][0] + 10, snake[0][1])
        turnrdown -= 1
    elif snake_direction == "DOWN" and turnrdown == 1:
        snake[2] = (snake[2][0], snake[2][1] + 10)
        snake[1] = (snake[1][0], snake[1][1] + 10)
        snake[0] = (snake[0][0] + 10, snake[0][1])
        turnrdown -= 1

    elif snake_direction == "DOWN" and turnldown == 2:
        snake[2] = (snake[2][0], snake[2][1] + 10)
        snake[1] = (snake[1][0] - 10, snake[1][1])
        snake[0] = (snake[0][0] - 10, snake[0][1])
        turnldown -= 1
    elif snake_direction == "DOWN" and turnldown == 1:
        snake[2] = (snake[2][0], snake[2][1] + 10)
        snake[1] = (snake[1][0], snake[1][1] + 10)
        snake[0] = (snake[0][0] - 10, snake[0][1])
        turnldown -= 1
    

# 游戏主循环
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake_direction == "RIGHT":
                snake_direction = "RIGHT"
            elif event.key == pygame.K_RIGHT and snake_direction == "UP":
                snake_direction = "RIGHT"
                turnuri=2
            elif event.key == pygame.K_RIGHT and snake_direction == "DOWN":
                snake_direction = "RIGHT"
                turndri=2  
            elif event.key == pygame.K_LEFT and snake_direction == "LEFT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_LEFT and snake_direction == "DOWN":
                snake_direction = "LEFT"
                turndle =2
            elif event.key == pygame.K_LEFT and snake_direction == "UP":
                snake_direction = "LEFT"
                turnule =2
            elif event.key == pygame.K_UP and snake_direction == "UP":
                snake_direction = "UP"
            elif event.key == pygame.K_UP and snake_direction == "RIGHT":
                snake_direction = "UP"
                turnrup=2
            elif event.key == pygame.K_UP and snake_direction == "LEFT":
                snake_direction = "UP"
                turnlup=2
            elif event.key == pygame.K_DOWN and snake_direction == "DOWN":
                snake_direction = "DOWN"
            elif event.key == pygame.K_DOWN and snake_direction == "RIGHT":
                snake_direction = "DOWN"
                turnrdown=2
            elif event.key == pygame.K_DOWN and snake_direction == "LEFT":
                snake_direction = "DOWN"
                turnldown=2

    move_snake()

    # 检查是否吃到了食物
    if snake[0] == food_pos:
        snake.append((0, 0))
        food_pos = (random.randint(0, WIDTH // 10 - 1) * 10, random.randint(0, HEIGHT // 10 - 1) * 10)

    # 检查是否撞到墙或者自己
    

    # 绘制贪吃蛇和食物
    draw_snake_and_food()

    # 控制游戏速度
    clock.tick(snake_speed)

# 游戏结束
pygame.quit()

