import pygame
import pygame_menu


class Game_Over_Menu:
    def __init__(self, main_menu, screen, score,
                 name, hight_name, hight_score):
        """Создание меню завершения игры"""
        self.main_menu = main_menu
        my_theme = pygame_menu.Theme(background_color=(0, 0, 0, 255),
                                     title_background_color=(0, 0, 0, 0),
                                     title_font_shadow=True,
                                     widget_padding=25)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/image/cosmos.jpg"),
            (screen.get_rect().width, screen.get_rect().height))
        self.screen = screen
        self.IsActive = True
        self.menu = pygame_menu.Menu("", 700, 800,
                                     theme=my_theme)

        text_color = (255, 255, 255)
        font = "assets/ofont.ru_Fixedsys.ttf"

        self.menu.add.label(f"{name}, your score {score}",
                            font_color=text_color,
                            font_name=font,
                            font_size=44)
        self.menu.add.label(f"Best score: {hight_name} - {hight_score}",
                            font_color=text_color,
                            font_name=font,
                            font_size=36)
        self.menu.add.button('Restart', self.start_the_game,
                             font_color=text_color,
                             font_name=font,
                             font_size=36)
        self.menu.add.button('Exit', self.in_main_menu,
                             font_color=text_color,
                             font_name=font,
                             font_size=36)

    def update(self):
        """Обновление меню завершения игры"""
        self.screen.blit(self.image, (0, 0))
        events = pygame.event.get()
        if self.menu.is_enabled():
            self.menu.update(events)
            self.menu.draw(self.screen)
        pygame.display.update()

    def start_the_game(self):
        """Начать игру"""
        self.main_menu.IsActive = False
        self.IsActive = False

    def in_main_menu(self):
        """Выход в главное меню"""
        self.main_menu.IsActive = True
        self.IsActive = False
