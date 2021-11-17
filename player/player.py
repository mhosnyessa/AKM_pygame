from .entity import Entity
import pygame
from sprite_handler import sprite_handler
import os
import sys
sys.path.append('..')
# import sys

# sys.path.insert(1, os.getcwd())


class Player(Entity):

    def __init__(self, x, y, window, player_sprite):
        super().__init__(x, y, window)
        self.speed = 5
        self.img.blit(
            sprite_handler.SpriteHandler.sprite_surface_converter(player_sprite, 1, 6)[0], (0, 0))

    def move_by_keys(self, keys):
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # left
            self.moveBy(-self.speed, 0)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # right
            self.moveBy(self.speed, 0)
        if keys[pygame.K_w] or keys[pygame.K_UP]:  # up
            self.moveBy(0, -self.speed)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # down
            self.moveBy(0, self.speed)
