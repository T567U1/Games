import pygame, random

class Food():
    def __init__(self, display):
        self.x, self.y = display
        self.x1 = self.x / 2
        self.y1 = self.y / 2
        self.color = pygame.Color(255, 0, 0) #red
        self.exist = True
        self.location = self.food_pos()

    def get_food_status(self, head):
        return self.food.colliderect(head)

    def food_pos(self):
        if self.exist:
            self.x1 = random.randint(0, self.x - self.y)
            self.y1 = random.randint(0, self.x - self.y)
            self.exist = False
            self.location = [self.x1, self.y1, 10, 10]
            return self.location
        return self.location

    def get_color(self):
        return self.color
