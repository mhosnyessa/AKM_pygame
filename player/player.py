# from os import X_OK
import pygame
# from core import WIN

hello = "hi"


# class Obj():
#     def __init__(self, name):
#         self.name = name

#     def print_hi(self):
#         print(hello, 'from Obj\n', ' name: ', self.name)


class Player:
    size = w, h = 50, 50
    color = (100, 50, 3)
    position_x = 0
    position_y = 0
    speed = 5

    def __init__(self, x: int, y: int, window: pygame.Surface, size=size, color=color):
        self.position_x = x
        self.position_y = y
        self.position = x, y
        self.window = window
        self.size = self.w, self.h = size

    def draw(self):
        pygame.draw.rect(self.window, self.color,
                         (self.position_x, self.position_y, self.w, self.h))

    def moveBy(self, x, y):
        x = int(x)
        y = int(y)
        self.is_off_screen()
        if(0 <= self.position_x and self.position_x <= self.window.get_width()):
            self.position_x += x
            self.position_y += y
            self.draw()

    def moveTo(self, x, y):
        x = int(x)
        y = int(y)
        self.is_off_screen()
        if(0 <= x and x <= self.window.get_width()):
            self.position_x = x
            self.draw()

    def is_off_screen(self):
        pass
        if(0 <= self.position_x
            and self.position_x <= self.window.get_width() and
                self.position_y <= self.window.get_height()):
            return True
