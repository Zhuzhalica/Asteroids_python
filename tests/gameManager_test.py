import unittest
import pygame
from Scripts import game_manager


class Game_Manager_Tests(unittest.TestCase):
    def test_in_screen(self):
        screen = pygame.display.set_mode((10, 10))
        position = pygame.Vector2(5, 5)
        self.assertTrue(game_manager.in_screen(screen, position))

        position = pygame.Vector2(11, 5)
        self.assertFalse(game_manager.in_screen(screen, position))

        position = pygame.Vector2(-1, 5)
        self.assertFalse(game_manager.in_screen(screen, position))

        position = pygame.Vector2(5, 11)
        self.assertFalse(game_manager.in_screen(screen, position))

        position = pygame.Vector2(5, -1)
        self.assertFalse(game_manager.in_screen(screen, position))

        position = pygame.Vector2(0, 0)
        self.assertTrue(game_manager.in_screen(screen, position))

        position = pygame.Vector2(10, 10)
        self.assertTrue(game_manager.in_screen(screen, position))
