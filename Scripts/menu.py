import pygame
import pygame_menu


class Menu:
    def __init__(self, screen=pygame.display.set_mode((800, 450))):
        my_theme = pygame_menu.Theme(background_color=(0, 0, 0, 0),
                                     title_background_color=(0, 0, 0, 0),
                                     title_font_shadow=True,
                                     widget_padding=30)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/image/background.jpg"),
            (screen.get_rect().width, screen.get_rect().height))
        self.screen = screen
        self.IsActive = True
        self.menu = pygame_menu.Menu("", 800, 800,
                                     theme=my_theme)

        text_color = (255, 255, 255)
        font = pygame.font.Font("assets/ofont.ru_Fixedsys.ttf", 36)
        self.menu.add.button('Play', self.start_the_game, font_name=font,
                             font_color=text_color)
        self.menu.add.text_input('Name: ', default='Player', font_name=font,
                                 font_color=text_color)
        self.menu.add.button('Quit', pygame_menu.events.EXIT, font_name=font,
                             font_color=text_color)

    def update(self):
        self.screen.blit(self.image, (0, 0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if self.menu.is_enabled():
            self.menu.update(events)
            self.menu.draw(self.screen)
        pygame.display.update()

    def start_the_game(self):
        self.player_name = self.menu.get_widgets()[1].get_value()
        self.IsActive = False
