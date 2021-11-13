import pygame
from .player import Player
import random


# class Child(player.Obj):
#     def __init__(self) -> None:
#         super().__init__('Muhammed')

#     def print_name_from_child(self,):
#         print(self.name)


# child = Child()
# child.print_hi()
# child.print_name_from_child()


class Villain(Player):

    def __init__(self, window: pygame.Surface, size=(50, 50), color=(100, 200, 100), x: int = 100, y: int = 100):
        self.size = self.w, self.h = 20, 20
        super().__init__(x, y, window)
        # self.speed = self.speed* 0.2
        self. __draw_random()
        self.repetitiveCounterX = 0
        self.repetitiveCounterY = 0
        self.maxRepeat = 3
        self.random_point = self.randomPointX, self.randomPointY = random.randint(
            0, self.window.get_width()), random.randint(0, self.window.get_height())

    def is_collided_with(self, obj):
        pass

    def __draw_random(self):
        self.position_x = random.randint(0, self.window.get_width())
        self.position_y = random.randint(0, self.window.get_height())

        self.color = self.random_color()
        self.draw()

    def move_random(self):
        # random_point = x, y = random.randint(
        #     0, self.window.get_width()), random.randint(0, self.window.get_height())
        if self.position_x < self.randomPointX:
            self.position_x += self.speed
            self.repetitiveCounterX += 1
            self.repetitiveCounterY = 0

        if self.position_x > self.randomPointX:
            self.position_x -= self.speed
            self.repetitiveCounterX += 1
            self.repetitiveCounterY = 0

        if self.position_y < self.randomPointY:
            self.position_y += self.speed
            self.repetitiveCounterY += 1
            self.repetitiveCounterX = 0

        if self.position_y > self.randomPointY:
            self.position_y -= self.speed
            self.repetitiveCounterY += 1
            self.repetitiveCounterX = 0

        self.position = self.position_x, self.position_y

        if self.repetitiveCounterX > self.maxRepeat or self.repetitiveCounterY >= self.maxRepeat:
            self.__random_point_canvas()

        # if self.position == self.random_point:
        if abs(
                self.position_x - self.randomPointX) <= self.speed and abs(
                    self.position_x - self.randomPointX) <= self.speed:
            self.__random_point_canvas()
            print('hello there')
            pass

        if self.repetitiveCounterX > self.maxRepeat or self.repetitiveCounterY >= self.maxRepeat:
            self.__random_point_canvas()
            pass

        self.draw()
        # self.moveBy(random.random() * self.speed / 2,
        #             random.random() * self.speed / 2)

    def random_color(self):
        color = [0, 0, 0]
        for i in range(3):
            color[i] = random.randint(0, 255)
        return color

    def __random_point_canvas(self):
        self.random_point = self.randomPointX, self.randomPointY = random.randint(
            0, self.window.get_width()), random.randint(0, self.window.get_height())

    def __del__():
        pass

    def killOneself(self):
        pass
