import unittest
import pygame
from Scripts.UFO import UFO
from Scripts.space_ship import SpaceShip
from pygame.sprite import Group

pygame.init()
screen = pygame.display.set_mode((800, 450))
player = SpaceShip(screen)


class UFO_Tests(unittest.TestCase):
    def test_empty_create(self):
        result = UFO(player, Group(), screen=screen)
        self.assertEqual(str(result.screen),
                         str(UFO(player, Group()).screen))

    # def test_update(self):
    #     test = UFO(player, Group())
    #     test.position = position()
    #     result = UFO(player, Group())
    #     result.position = pygame.Vector2(0, 0) + test.speed * test.direction
    #     result.stay_in_screen()
    #
    #     test.update()
    #
    #     self.assertEqual(result.position, test.position)

    def test_shoot(self):
        b = Group()
        test = UFO(player, b)
        test.frequency_bullets = 0

        self.assertEqual(test.count_frames_bullet, 0)
        self.assertEqual(len(b), 0)
        test.update()
        self.assertEqual(test.count_frames_bullet, 1)
        self.assertEqual(len(b), 0)
        test.update()
        self.assertEqual(test.count_frames_bullet, 1)
        self.assertGreaterEqual(len(b), 0)
        test.update()
        self.assertEqual(test.count_frames_bullet, 1)
        self.assertGreaterEqual(len(b), 0)
        self.assertLessEqual(len(b), 2)

    def test_stay_in_screen(self):
        screen = pygame.display.set_mode((10, 10))
        test = UFO(player, Group(), screen=screen)

        test.position = pygame.Vector2(15, 5)
        result_position = pygame.Vector2(5, 5)
        test.stay_in_screen()
        self.assertEqual(test.position, result_position)

        test.position = pygame.Vector2(-5, 5)
        result_position = pygame.Vector2(5, 5)
        test.stay_in_screen()
        self.assertEqual(test.position, result_position)

        test.position = pygame.Vector2(5, 15)
        result_position = pygame.Vector2(5, 5)
        test.stay_in_screen()
        self.assertEqual(test.position, result_position)

        test.position = pygame.Vector2(5, -5)
        result_position = pygame.Vector2(5, 5)
        test.stay_in_screen()
        self.assertEqual(test.position, result_position)
