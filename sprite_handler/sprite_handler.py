import pygame
import os


class SpriteHandler:
    @staticmethod
    def sprite_surface_converter(sprite: pygame.Surface,
                                 number_vr, number_hr, height=40, width=40, colorKey=(0, 0, 0)):
        player_sprite = pygame.image.load(os.path.join(
            'assets', '2 GraveRobber', 'GraveRobber_walk.png')).convert_alpha()
        if sprite == 0:
            sprite = player_sprite

        # happens to be a 1 by 6 sprite sheet
        sprite_h = sprite.get_height()
        sprite_w = sprite.get_width()
        char_pre_h = sprite_h / number_vr
        char_pre_w = sprite_w / number_hr

        imgs = []

        for i in range(0, number_vr):
            for j in range(0, number_hr):
                image = pygame.Surface(
                    (char_pre_w, char_pre_h)).convert_alpha()

                image.blit(sprite, (j * char_pre_w, i * char_pre_h),
                           (0, 0, char_pre_w, char_pre_h))

                image = pygame.transform.scale(
                    image, (width, height))

                image.set_colorkey(colorKey)
                imgs.append(image)
        return imgs
