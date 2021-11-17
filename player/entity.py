# from os import X_OK
import random
import pygame
# from core import WIN

hello = "hi"


# class Obj():
#     def __init__(self, name):
#         self.name = name

#     def print_hi(self):
#         print(hello, 'from Obj\n', ' name: ', self.name)


class Entity:
    size = w, h = 50, 50
    color = (100, 50, 3)
    position_x = 0
    position_y = 0
    speed = 50

    def __init__(self, x: int, y: int, window: pygame.Surface, size=size, color=color):
        self.position_x = x
        self.position_y = y
        self.position = x, y
        self.window = window
        self.color = self.random_color()
        self.size = self.w, self.h = size
        self.img = pygame.Surface((self.w, self.h))
        self.img.fill(self.color)
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self):
        # pygame.draw.rect(self.window, self.color,
        #                  (self.position_x, self.position_y, self.w, self.h))
        self.window.blit(self.img, (self.position_x, self.position_y), )

    def random_color(self):
        color = [0, 0, 0]
        for i in range(3):
            color[i] = random.randint(0, 255)

        return color

    def moveBy(self, x, y):
        # x = int(x)
        # y = int(y)
        # self.is_off_screen()
        # if 0 <= self.position_y + y and self.position_y + y + self.h <= self.window.get_width() and 0 <= self.position_x + x and self.position_x + x + self.w <= self.window.get_width():
        # if not self.is_off_screen():
        self.position_x += x
        self.position_y += y
        self.draw()

    def moveTo(self, x, y):
        x = int(x)
        y = int(y)
        self.is_off_screen()
        if(0 <= self.position_x - self.speed and self.position_x + self.speed <= self.window.get_width()):
            self.position_x = x
            self.draw()

    # def is_off_screen(self):
    #     pass
    #     if(0 <= self.position_x
    #         and self.position_x <= self.window.get_width() and
    #             self.position_y <= self.window.get_height()):
    #         return True

    # def get_width(self):
    #     self.size = self.w, self.h
    #     return self.size
    def is_off_screen(self):
        x = self.position_x
        y = self.position_y
        w = self.w
        h = self.h
        window_w = self.window.get_width()
        window_h = self.window.get_height()
        return (x < 0 or x + w > window_w or y < 0 or y + h > window_h)
