import pygame
from game import Game
from menu import Menu


def run():
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("Asteroids")
    menu = Menu(screen)
    game = None

    while True:
        if not menu.IsActive:
            if game is None:
                game = Game(screen)

            if not game.game_over:
                game.game_update()
            else:
                game = None
        else:
            menu.update()


run()
