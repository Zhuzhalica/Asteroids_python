import pygame
import pygame_menu
from button import Button

class Menu:
    def __init__(self, screen):  
        self.mytheme = pygame_menu.Theme(background_color=(0, 0, 0, 0), # transparent background
                title_background_color=(0, 0, 0, 0),
                title_font_shadow=True,
                widget_padding=30)
        self.image = pygame.transform.scale(pygame.image.load("image\\background.jpg"), (screen.get_rect().width, screen.get_rect().height))
        self.screen = screen
        self.IsActive = True
        self.menu = pygame_menu.Menu("", 300, 400,
                            theme=self.mytheme)
        
        # self.menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=self.set_difficulty)
        self.menu.add.button('Play', self.start_the_game)
        self.menu.add.text_input('Name:', default='Player')
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        
    
    def update(self):
        
        self.screen.blit(self.image, (0,0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if self.menu.is_enabled():
            self.menu.update(events)
            self.menu.draw(self.screen)
        pygame.display.update()
            


    def start_the_game(self):
        self.IsActive = False




