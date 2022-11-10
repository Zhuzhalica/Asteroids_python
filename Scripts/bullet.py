import math
import pygame

import Scripts.game_manager as game_manager


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen=pygame.display.set_mode((800, 450)),
                 space_ship=None, add_angle=0):
        """иницилизация пули"""
        super(Bullet, self).__init__()

        if space_ship is not None:
            self.screen = screen

            self.image = pygame.transform.rotate(
                pygame.image.load("assets/image/bullet.png"),
                space_ship.angle)

            self.rect = self.image.get_rect()
            self.speed = 7

            d = space_ship.direction.copy()
            d.rotate_ip(add_angle)
            self.direction = d.copy()

            position = space_ship.position.copy()
            position.y -=\
                space_ship.image.get_size()[1] *\
                math.cos(math.radians(space_ship.angle - add_angle)) / 2
            position.x -=\
                space_ship.image.get_size()[0] *\
                math.sin(math.radians(space_ship.angle - add_angle)) / 2
            self.position = position
        else:
            raise ValueError('Space_ship is None')

    def update(self):
        """Обновляем позицию пули"""
        self.position += self.direction * self.speed
        self.rect.center = self.position

    def draw(self):
        """Отрисовываем пулю на экране"""
        self.screen.blit(self.image, self.position)

    def in_screen(self):
        """Находится ли пуля в границах экарана"""
        return game_manager.in_screen(self.screen, self.position)
