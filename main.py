import pygame
from game import Game
from menu import Menu


def run():
    pygame.mixer.pre_init(44100, -16, 1, 512) 
    pygame.init()
    pygame.mixer.music.load("sounds/background_music.mp3")
 
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("Asteroids")
    menu = Menu(screen)
    game = None
    pygame.mixer.music.play(-1)
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
