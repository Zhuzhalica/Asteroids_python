import unittest
import pygame
from statistic import Stat
from space_ship import SpaceShip
from asteroid import Asteroid
from UFO import UFO
import os.path

screen = pygame.display.set_mode((800, 450))
player = SpaceShip(screen)


class Statistic_Tests(unittest.TestCase):
    def test_create_without_player(self):
        with self.assertRaises(ValueError) as e:
            Stat(screen=screen, space_ship=None)

        self.assertEqual("Space_ship is None", e.exception.args[0])

    def test_create_without_screen(self):
        result = Stat(screen=screen, space_ship=player)
        test = Stat(space_ship=player)

        self.assertEqual(result.screen, test.screen)

    def test_make_stat(self):
        test = Stat(space_ship=player)
        asteroid = Asteroid(generator=None,
                            screen=screen,
                            start_position=pygame.Vector2(0, 10),
                            size=pygame.Vector2(42, 42),
                            direction=pygame.Vector2(),
                            speed=0,
                            filename="assets/image/image_asteroids/planet1.png")
        test.make_stat(asteroid)
        self.assertEqual(50, test.score)
        ufo = UFO()
        test.make_stat(ufo)
        self.assertEqual(250, test.score)

    def test_really_update_high_score(self):
        test = Stat(space_ship=player)
        test.high_score = 0
        test.high_name = "Player1"
        test.score = 100
        test.player_name = "Player2"
        test.update_high_score()
        self.assertEqual(100, test.high_score)
        self.assertEqual("Player2", test.high_name)
        self.assertTrue(os.path.exists(test.save_file_path))

    def test_unupdate_high_score(self):
        test = Stat(space_ship=player)
        test.high_score = 100
        test.high_name = "Player1"
        test.score = 0
        test.player_name = "Player2"
        test.update_high_score()
        self.assertEqual(100, test.high_score)
        self.assertEqual("Player1", test.high_name)
        self.assertTrue(os.path.exists(test.save_file_path))