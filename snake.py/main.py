import pygame, sys, random
from objects import snake, food, controls

#start pyGame
pygame.init()
pygame.font.init()
sleep = pygame.time.Clock()
#colors
black = (0, 0, 0) #background color
blue = (0, 0, 255) #snake color
white = (255, 255, 255)
red = (255, 255, 255)
#set display
display = pygame.display.set_mode((1000, 500))
pygame.display.update()
pygame.display.set_caption('Snake')
display_size = display.get_size()
font = pygame.font.SysFont('simsunextb', 24)
#controls
controls_ = controls.Controls()
#initiate snake
snake_head = snake.Snake(display_size)
#initiate food
food_ = food.Food(display_size)
#moving
x, y = [10, 0]

def collision(snake):
    if snake.get_snake_head() in snake.get_body()[1:]:
        return 0
    return 1

def print_snake(parts):
    if not parts:
        return
    #set snake flow
    pygame.draw.rect(display, blue, parts[0])
    return print_snake(parts[1:])

def game_over():
    text = font.render('Game Over Press Esc to exit', True, red, black)
    display_game_over = text.get_rect()
    display_game_over.center = (display_size[0] // 2, display_size[1] // 2)
    while True:
        display.fill(white)
        display.blit(text, display_game_over)
        for event in pygame.event.get():
            #quit by closing pygames screen or pressing ESC
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == 27):
                return

        pygame.display.update()

def game_on():
    while collision(snake_head):
        for event in pygame.event.get():
            #quit by closing pygames screen or pressing ESC
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == 27):
                return
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

    game_over()

game_on()
pygame.quit()
quit()
