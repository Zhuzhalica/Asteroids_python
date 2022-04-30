import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, title, font, y, width=0, height=0):
        self.title = title
        self.text = font.render(self.title, 1, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(400, y))
        self.rect = pygame.Rect(200, self.text_rect.y - 25, 400, 76)
        self.isPressed = False

    def check(self, mouse_event):
        if self.rect.collidepoint(mouse_event):
            self.isPressed = True

    def update(self, screen):
        if not self.isPressed:
            pygame.draw.rect(screen, (255, 255, 255), (200, self.text_rect.y - 25, 400, 76))
            screen.blit(self.text, self.text_rect)
