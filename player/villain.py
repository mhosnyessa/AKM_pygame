import pygame
from .entity import Entity
import random
import math


# class Child(player.Obj):
#     def __init__(self) -> None:
#         super().__init__('Muhammed')

#     def print_name_from_child(self,):
#         print(self.name)


# child = Child()
# child.print_hi()
# child.print_name_from_child()


class Villain(Entity):

    def __init__(self, window: pygame.Surface, size=(30, 30), color=(100, 200, 100), x: int = 100, y: int = 100):
        super().__init__(x, y, window, size)
        self.size = self.w, self.h = size
        # self.speed = self.speed* 0.2
        self. __draw_random()
        self.repetitiveCounterX = 0
        self.repetitiveCounterY = 0
        self.speed = 4
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
        # if self.is_off_screen():
        #     del()
        rx = self.randomPointX
        ry = self.randomPointY
        x = self.position_x
        y = self.position_y

        angle = math.atan2(ry - y, rx - x)

        x_vel = math.cos(angle) * self.speed
        y_vel = math.sin(angle) * self.speed

        self.moveBy(x_vel, y_vel)

        # if self.position_x < self.randomPointX:
        #     self.position_x += self.speed
        #     self.repetitiveCounterX += 1
        #     self.repetitiveCounterY = 0

        # if self.position_x > self.randomPointX:
        #     self.position_x -= self.speed
        #     self.repetitiveCounterX += 1
        #     self.repetitiveCounterY = 0

        # if self.position_y < self.randomPointY:
        #     self.position_y += self.speed
        #     self.repetitiveCounterY += 1
        #     self.repetitiveCounterX = 0

        # if self.position_y > self.randomPointY:
        #     self.position_y -= self.speed
        #     self.repetitiveCounterY += 1
        #     self.repetitiveCounterX = 0

        # self.position = self.position_x, self.position_y

        # if self.repetitiveCounterX > self.maxRepeat or self.repetitiveCounterY >= self.maxRepeat:
        #     self.__random_point_canvas()

        # if self.position == self.random_point:
        # if abs(
        #         self.position_x - self.randomPointX) <= self.speed and abs(
        #             self.position_x - self.randomPointX) <= self.speed:
        #     self.__random_point_canvas()
        if abs(x - rx) <= x_vel or abs(y - ry) <= y_vel:
            self.__random_point_canvas()

        # if self.repetitiveCounterX > self.maxRepeat or self.repetitiveCounterY >= self.maxRepeat:
        #     self.__random_point_canvas()
        # self.draw()
        # self.moveBy(random.random() * self.speed / 2,
        #             random.random() * self.speed / 2)

    def random_color(self):
        color = [0, 0, 0]
        for i in range(3):
            color[i] = random.randint(0, 255)
        return color

    def __random_point_canvas(self):
        self.random_point = self.randomPointX, self.randomPointY = random.randint(
            0, self.window.get_width() - self.w), random.randint(0, self.window.get_height() - self.h)

    # def killOneself(self):
    #     del()
    #     pass

    def collide(obj1, obj2):
        # obj1 = obj1.img
        # obj2 = obj2.img
        offset_x = obj2.position_x - obj1.position_x
        offset_y = obj2.position_y - obj1.position_y

        return (obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None)
