import pygame
from game import Game
from menu import Menu
from game_over_menu import Game_Over_Menu


def run():
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.mixer.music.load("sounds/background_music.mp3")

    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("Asteroids")
    menu = Menu(screen)
    game = None
    game_over = None
    pygame.mixer.music.play(-1)
    while True:
        if menu.IsActive:
            menu.update()
        else:
            if game is None and game_over is None:
                game = Game(screen, menu.player_name)

            if game is not None and not game.game_over:
                game.game_update()
            elif game is not None and game.game_over:
                game.stat.update_high_score()
                game_over = Game_Over_Menu(menu, screen,
                                           game.stat.score,
                                           menu.player_name,
                                           game.stat.high_name,
                                           game.stat.high_score)
                game = None
            elif game_over is not None and game_over.IsActive:
                game_over.update()

            if game_over is not None and not game_over.IsActive:
                game_over = None


run()
