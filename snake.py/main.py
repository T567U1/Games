import pygame, sys, random
from objects import snake, food

#start pyGame
pygame.init()
sleep = pygame.time.Clock()
#colors
black = (0, 0, 0)
#set display
display = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake')
display_size = display.get_size()
#initiate snake
snake = snake.Snake((0, 0, 255), display_size)
#initiate food
food = food.Food(display_size)
#while 1 game is on
game_on = 1
#moving
x, y = [10, 0]

while game_on:
    for event in pygame.event.get():
        #quit by closing pygames screen or pressing ESC
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == 27):
            game_on = 0
        if event.type == pygame.KEYDOWN:
            snake.controls(event.key)

    display.fill(black)
    #set snake flow
    snake.controls()
    #update snake position
    pygame.draw.rect(display, food.get_color(), food.food_pos())
    pygame.draw.rect(display, snake.get_color(), snake.get_snake())
    pygame.display.update()
    sleep.tick(5)

pygame.quit()
quit()
