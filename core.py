import os
import pygame
from player.player import Player
from player import villain
# this is the main branch
pygame.font.init()
pygame.init()
GAME_NAME = "AKM"
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# below is when you want it to be full screen
# WIN = pygame.display.set_mode()
PADDING = 15
# player_sprite = pygame.image.load(os.path.join(
#     'assets', '2 GraveRobber', 'GraveRobber_walk.png')).convert_alpha()
heart = pygame.image.load(
    os.path.join("assets", "heart.png"))
heartHeight = 40
heart = pygame.transform.scale(
    heart, (heart.get_width() * (heartHeight / heart.get_height()), 40))

FPS = 60
BG = GREY = (100, 100, 100)
BLACK = (0, 0, 0)
# main_font = pygame.font.SysFont("comicsans", 50)
# lost_font = pygame.font.SysFont("comicsans", 60)
pygame.display.set_caption(f"Now you'r playing :- {GAME_NAME} game")
# Load images


def main():
    run = True
    level = 0
    lives = 3
    enemy_vel = 1
    player_vel = 5
    laser_vel = 5
    player = Player(100, 130, WIN, 0)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    villians = []
    for i in range(15):
        villians.append(villain.Villain(WIN))

    def redraw_window():
        WIN.fill(color=BG)
        # draw text
        # pygame.display.update()

    main_font = pygame.font.SysFont("comicsans", 65)
    score = 0
    while run:

        pygame.time.Clock().tick(FPS)
        redraw_window()
        for i in range(1, lives + 1):
            WIN.blit(
                heart, (int(WIN.get_width() - (heart.get_width() + PADDING) * i), PADDING))
        score_label = main_font.render(f"score: {score}", 1, (255, 255, 255))
        WIN.blit(score_label, (int(WIN.get_width() / 2 - score_label.get_width() / 2),
                               int(20)))

        player.draw()
        if villians:
            for i in villians:
                i.move_random()
                # if i.is_off_screen() or i.collide(player):
                if i.collide(player):
                    villians.remove(i)
                    score += 1

            keys = pygame.key.get_pressed()
            player.move_by_keys(keys)
        else:
            label = main_font.render(f"you WON!!", 1, (255, 255, 255))
            WIN.blit(label, (int(WIN.get_width() / 2 - label.get_width() / 2),
                     int(WIN.get_height() / 2 - label.get_height())))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


if __name__ == '__main__':
    main()
