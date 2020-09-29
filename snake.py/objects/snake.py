import pygame

class Snake:
    def __init__(self, color, display):
        self.x, self.y = display
        self.color = color
        self.body = [200,150,10,10]
        self.prev = [-10, 0]
        self.direction = [10, 0]

    def get_snake(self):
        return self.body

    def get_color(self):
        return self.color

    def set_body(self, arr):
        self.body = [arr[0] + self.body[0], arr[1] + self.body[1], 10, 10]
        #check for boarders
        if self.body[0] > self.x:
            self.body[0] = 0
        if self.body[0] < 0:
            self.body[0] = self.x

        if self.body[1] > self.y:
            self.body[1] = 0
        if self.body[1] < 0:
            self.body[1] = self.y

    def controls(self, key = 0):
        controls_ = {
            119: [0, -10], #Up
            115: [0, 10], #Down
            97: [-10, 0], #left
            100: [10, 0] #Right
        }
        prev = {
            119: [0, 10], #Up
            115: [0, -10], #Down
            97: [10, 0], #left
            100: [-10, 0] #Right
        }
        if key not in controls_:
            self.set_body(self.direction)
        else:
            #if given command is to comeback or same direction
            if self.prev == controls_[key] or self.direction == controls_[key]:
                return
            self.prev = prev[key]
            self.direction = controls_[key]
            self.set_body(controls_[key])
