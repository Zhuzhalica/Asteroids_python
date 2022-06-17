import unittest
import pygame
from game import Game

screen = pygame.display.set_mode((800, 450))


class Game_Tests(unittest.TestCase):
    def test_empty_create(self):
        result = Game(screen)
        self.assertEqual(str(result.screen), str(Game().screen))

    def test_update_space_ship_death(self):
        test = Game(screen)
        test.space_ship.health = 0
        test.game_update()
        self.assertTrue(test.game_over)

    def test_update_space_ship_live(self):
        test = Game(screen)
        test.game_update()
        self.assertFalse(test.game_over)
