import pygame

snake = [[200,150,10,10], [190,150,10,10], [180,150,10,10], [170,150,10,10]]
class Snake:
    def __init__(self, display, body = snake, next = None):
        self.limit_x, self.limit_y = display
        self.body = body

    def get_snake(self):
        return self.body

    def get_snake_head(self):
        return self.body[0]

    def get_body(self):
        return self.body

    def move(self, x, y):
        new_head = self.get_snake_head()[:]
        new_head[0] += x
        new_head[1] += y

        if new_head[0] > self.limit_x:
            new_head[0] = 0
        if new_head[0] < 0:
            new_head[0] = self.limit_x

        if new_head[1] > self.limit_y:
            new_head[1] = 0
        if new_head[1] < 0:
            new_head[1] = self.limit_y

        self.body.insert(0, new_head)
        self.body.pop()

    def add_part(self, x, y):
        new_head = self.get_snake_head()[:]
        new_head[0] += x
        new_head[1] += y
        self.body.insert(0, new_head)
