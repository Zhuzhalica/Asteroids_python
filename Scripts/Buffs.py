from enum import Enum
import pygame


class Buff_Item(pygame.sprite.Sprite):
    def __init__(self, enum, screen=pygame.display.set_mode((800, 450)),
                 position=pygame.Vector2()):
        """Создание бонусного предмета"""
        pygame.sprite.Sprite.__init__(self)
        try:
            if enum in Buffs:
                self.screen = screen
                self.position = position
                self.image = enum.value
                self.rect = self.image.get_rect()
                self.rect.center = self.position
                self.enum_type = enum
        except TypeError:
            raise ValueError(f'{enum} doesn`t exist in Buffs')

    def draw(self):
        """отрисовка бонусного предмета"""
        self.screen.blit(self.image, self.position)


class Buffs(Enum):
    """Типы бонусных предметов"""
    Shield = pygame.transform.scale(
        pygame.image.load("assets/image/space-ship-pr.png"), (30, 30))
    HP = pygame.transform.scale(
        pygame.image.load("assets/image/space-ship.png"), (30, 30))
    Triple_Gun = pygame.transform.scale(
        pygame.image.load("assets/image/bullet.png"), (30, 30))
