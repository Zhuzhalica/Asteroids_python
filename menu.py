import pygame
from button import Button


class Menu:

    def __init__(self, screen, font):
        self.screen = screen
        self.buttons = [Button("Start game", font, screen.get_rect().centery)]
        self.title = 'Asteroids'
        self.text = font.render(self.title, 1, (0, 0, 0))
        self.IsActive = True

    def update(self):
        if self.IsActive:
            for button in self.buttons:
                button.update(self.screen)
            self.screen.blit(self.text, self.text.get_rect(center=(400, 100)))
            self.IsActive = not self.buttons[0].isPressed
