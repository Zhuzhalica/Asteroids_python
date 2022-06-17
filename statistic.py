import pygame
from asteroid import Asteroid
from UFO import UFO
import os.path


class Stat:
    def __init__(self, screen=pygame.display.set_mode((800, 450)), space_ship=None, player_name=''):
        """Иницилизация игровой статистики"""
        if space_ship is not None:
            self.player = space_ship
            self.player_name = player_name
            self.screen = screen
            self.score = 0
            self.text_color = (255, 255, 255)
            self.font = pygame.font.Font("assets/ofont.ru_Fixedsys.ttf", 48)
            self.stat_image = self.font.render(str(self.score), True, self.text_color, (0, 0, 0))
            self.score_rect = self.stat_image.get_rect()
            self.save_file_path = 'save.txt'
            self.parse_save()
        else:
            raise ValueError("Space_ship is None")

    def parse_save(self):
        if os.path.exists(self.save_file_path):
            with open(self.save_file_path, "r") as f:
                line = f.readline()
                name, score = line.split(":")
                self.high_name = name
                self.high_score = int(score)
        else:
            self.high_name = ''
            self.high_score = 0

    def update_high_score(self):
        if self.score >= self.high_score:
            with open(self.save_file_path, "w") as f:
                f.write(f'{self.player_name}:{self.score}')
            self.high_score = self.score
            self.high_name = self.player_name

    def make_stat(self, enemy):
        if type(enemy) is Asteroid:
            self.score += int(100 * (enemy.image.get_size()[0] / enemy.max_size))
            enemy.death()
        elif type(enemy) is UFO:
            self.score += int(200 * (enemy.image.get_size()[0] / enemy.max_size))
            enemy.kill()

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
