import pygame
from pygame.sprite import Group


class Stat:
    def __init__(self, screen, space_ship):
        """Иницилизация игровой статистики"""
        self.player = space_ship
        self.screen = screen
        self.score = 0
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font("assets/ofont.ru_Fixedsys.ttf", 48)
        self.stat_image = self.font.render(str(self.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.stat_image.get_rect()
        self.high_score = 0

    def draw_stat(self):
        """Отображение статистика на экране"""
        self.stat_image = self.font.render(f"Score: {str(self.score)}", True, self.text_color)
        self.score_rect = self.stat_image.get_rect()
        self.score_rect.left = self.screen.get_rect().left + 50
        self.score_rect.bottom = 50

        self.draw_health()
        self.update_stat()

    def update_stat(self):
        """Обновление изображения статистика на экране"""
        self.screen.blit(self.stat_image, self.score_rect)

    def draw_health(self):
        """Отображение здоровья на экране"""
        for i in range(self.player.health):
            image = pygame.transform.scale(pygame.image.load("assets/image/space-ship.png"), (30, 30))
            rect = image.get_rect()
            rect.left = self.screen.get_rect().left + 50 + 40 * i
            rect.bottom = 90
            self.screen.blit(image, rect)
