import math
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, space_ship):
        """иницилизация пули"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.transform.rotate(pygame.image.load("image/bullet.png"), space_ship.angle)
        self.rect = self.image.get_rect()
        self.speed = 5
        self.direction = space_ship.direction.copy()
        position = space_ship.position.copy()
        position.y -= space_ship.image.get_size()[1] * math.cos(math.radians(space_ship.angle)) / 2
        position.x -= space_ship.image.get_size()[0] * math.sin(math.radians(space_ship.angle)) / 2

        self.position = position



    def update(self, space_ship):
        """Обновляем позицию пули"""
        self.position += self.direction * self.speed
        self.rect.center = self.positio


    def draw_bullet(self):
        """Отрисовываем пулю на экране"""
        self.screen.blit(self.image, self.position)
