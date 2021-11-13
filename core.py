
import pygame
from player.player import Player
from player import villain
pygame.font.init()

GAME_NAME = "AKM"
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
BG = GREY = (100, 100, 100)
BLACK = (0, 0, 0)
# main_font = pygame.font.SysFont("comicsans", 50)
# lost_font = pygame.font.SysFont("comicsans", 60)
pygame.display.set_caption(f"{GAME_NAME}")
# Load images


def main():
    run = True
    level = 0
    lives = 5

    enemy_vel = 1

    player_vel = 5
    laser_vel = 5

    player = Player(100, 130, WIN)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    villians = []
    for i in range(4):
        villians.append(villain.Villain(WIN))

    def redraw_window():
        WIN.fill(color=BG)
        # draw text
        # pygame.display.update()

    while run:
        pygame.time.Clock().tick(FPS)
        redraw_window()
        player.draw()
        for i in villians:
            i.move_random()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # left
            player.moveBy(-player_vel, 0)
        if keys[pygame.K_d]:  # right
            player.moveBy(player_vel, 0)
        if keys[pygame.K_w]:  # up
            player.moveBy(0, -player_vel)
        if keys[pygame.K_s]:  # down
            player.moveBy(0, player_vel)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


if __name__ == '__main__':
    main()
