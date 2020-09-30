import pygame, sys, random
from objects import snake, food, controls

#start pyGame
pygame.init()
sleep = pygame.time.Clock()
#colors
black = (0, 0, 0) #background color
blue = (0, 0, 255) #snake color
#set display
display = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake')
display_size = display.get_size()
#controls
controls_ = controls.Controls()
#initiate snake
snake_head = snake.Snake(display_size)
#initiate food
food_ = food.Food(display_size)
#while 1 game is on
game_on = 1
#moving
x, y = [10, 0]

def print_snake(parts):
    if not parts:
        return
    #set snake flow
    pygame.draw.rect(display, blue, parts[0])
    return print_snake(parts[1:])


while game_on:
    for event in pygame.event.get():
        #quit by closing pygames screen or pressing ESC
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == 27):
            game_on = 0
        if event.type == pygame.KEYDOWN:
            controls_.get_next(event.key)

    display.fill(black)
    #update snake position
    if food_.get_food_location() == snake_head.get_snake_head():
        snake_head.add_part(controls_.x, controls_.y)
        food_.food_eaten()

    snake_head.move(controls_.x, controls_.y)
    pygame.draw.rect(display, food_.get_color(), food_.get_food_location())
    print(snake_head.body)
    print_snake(snake_head.body)
    pygame.display.update()
    sleep.tick(3)

pygame.quit()
quit()
