import math
import pygame

import game_manager


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, space_ship):
        """иницилизация пули"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.transform.rotate(pygame.image.load("assets/image/bullet.png"), space_ship.angle)
        self.rect = self.image.get_rect()
        self.speed = 5
        self.direction = space_ship.direction.copy()
        position = space_ship.position.copy()
        position.y -= space_ship.image.get_size()[1] * math.cos(math.radians(space_ship.angle)) / 2
        position.x -= space_ship.image.get_size()[0] * math.sin(math.radians(space_ship.angle)) / 2

        self.position = position


    def update(self):
        """Обновляем позицию пули"""
        self.position += self.direction * self.speed
        self.rect.center = self.position


    def draw(self):
        """Отрисовываем пулю на экране"""
        self.screen.blit(self.image, self.position)

    def in_screen(self):
        return game_manager.in_screen(self.screen, self.position)