import unittest
import pygame
from Scripts.generator_UFO import Generator_UFO
from Scripts.space_ship import SpaceShip

pygame.init()
screen = pygame.display.set_mode((800, 450))
player = SpaceShip(screen)


class Generator_UFO_Tests(unittest.TestCase):
    def test_empty_create(self):
        result = Generator_UFO(player, screen=screen)
        self.assertEqual(str(result.screen),
                         str(Generator_UFO(player).screen))

    def test_make_UFO(self):
        result = Generator_UFO(player)
        result.make_UFO()
        self.assertEqual(1, len(result.ufos))

    def test_update(self):
        test = Generator_UFO(player)

        self.assertEqual(test.count, 0)
        self.assertEqual(len(test.ufos), 0)
        test.update()
        self.assertEqual(test.count, 1)
        self.assertEqual(len(test.ufos), 0)
        test.update()
        self.assertEqual(test.count, 1)
        self.assertGreaterEqual(len(test.ufos), 0)
        test.update()
        self.assertEqual(test.count, 1)
        self.assertGreaterEqual(len(test.ufos), 0)
        self.assertLessEqual(len(test.ufos), 2)
