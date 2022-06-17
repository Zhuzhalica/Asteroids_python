import math
import unittest
import pygame
from bullet import Bullet
from space_ship import SpaceShip

pygame.init()
screen = pygame.display.set_mode((800, 450))
player = SpaceShip(screen)


class Bullet_Tests(unittest.TestCase):
    def test_create_without_player(self):
        with self.assertRaises(ValueError) as e:
            Bullet(screen=screen, space_ship=None)

        self.assertEqual("Space_ship is None", e.exception.args[0])

    def test_create_without_screen(self):
        result = Bullet(screen=screen, space_ship=player)
        test = Bullet(space_ship=player)

        self.assertTrue(str(result.__dict__) == str(test.__dict__))

    def test_create_with_player(self):
        result = Bullet(space_ship=player)
        result.screen = screen
        result.speed = 7
        result.direction = player.direction.copy()
        position = player.position.copy()
        position.y -= player.image.get_size()[1] * math.cos(math.radians(player.angle)) / 2
        position.x -= player.image.get_size()[0] * math.sin(math.radians(player.angle)) / 2
        result.position = position

        test = Bullet(screen=screen, space_ship=player)

        self.assertTrue(str(result.__dict__) == str(test.__dict__))

    def test_create_with_add_angle(self):
        result = Bullet(screen=pygame.display.set_mode((1600, 900)),
                        space_ship=player)
        result.direction.rotate_ip(30)
        result.position.y = player.position.y - \
                            player.image.get_size()[1] * \
                            math.cos(math.radians(player.angle - 30)) / 2
        result.position.x = player.position.x - \
                            player.image.get_size()[0] * \
                            math.sin(math.radians(player.angle - 30)) / 2

        test = Bullet(space_ship=player, add_angle=30)

        self.assertEqual(str(result.__dict__), str(test.__dict__))

    def test_update(self):
        result = Bullet(space_ship=player)
        result.position += result.direction * result.speed
        result.rect.center = result.position

        test = Bullet(space_ship=player)
        test.update()

        self.assertTrue(str(result.__dict__) == str(test.__dict__))

    def test_in_screen(self):
        screen = pygame.display.set_mode((10, 10))
        result = Bullet(screen=screen, space_ship=player)

        result.position = pygame.Vector2(5, 5)
        self.assertTrue(result.in_screen())

        result.position = pygame.Vector2(11, 5)
        self.assertFalse(result.in_screen())

        result.position = pygame.Vector2(-1, 5)
        self.assertFalse(result.in_screen())

        result.position = pygame.Vector2(5, 11)
        self.assertFalse(result.in_screen())

        result.position = pygame.Vector2(5, -1)
        self.assertFalse(result.in_screen())

        result.position = pygame.Vector2(0, 0)
        self.assertTrue(result.in_screen())

        result.position = pygame.Vector2(10, 10)
        self.assertTrue(result.in_screen())
