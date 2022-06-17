import unittest
import pygame
from generator_asteroids import Generator
from asteroid import Asteroid


class Asteroid_Tests(unittest.TestCase):
    def test_empty_create(self):
        null_vector = pygame.Vector2()
        result = Asteroid(generator=None,
                          screen=pygame.display.set_mode((800, 450)),
                          start_position=null_vector.copy(),
                          size=null_vector.copy(),
                          direction=null_vector.copy(),
                          speed=0,
                          filename="assets/image/image_asteroids/planet1.png")

        self.assertEqual(str(result.__dict__), str(Asteroid().__dict__))

    def test_update(self):
        null_vector = pygame.Vector2()
        result = Asteroid(generator=None,
                          screen=pygame.display.set_mode((800, 450)),
                          start_position=pygame.Vector2(0, 10),
                          size=null_vector.copy(),
                          direction=pygame.Vector2(0, 1),
                          speed=10,
                          filename="assets/image/image_asteroids/planet1.png")

        test = Asteroid(generator=None,
                        screen=pygame.display.set_mode((800, 450)),
                        start_position=pygame.Vector2(0, 0),
                        size=null_vector.copy(),
                        direction=pygame.Vector2(0, 1),
                        speed=10,
                        filename="assets/image/image_asteroids/planet1.png")
        test.update()
        self.assertTrue(str(result.__dict__) == str(test.__dict__))

    def test_in_screen(self):
        null_vector = pygame.Vector2()
        screen = pygame.display.set_mode((10, 10))
        result = Asteroid(generator=None,
                          screen=screen,
                          start_position=null_vector.copy(),
                          size=null_vector.copy(),
                          direction=null_vector.copy(),
                          speed=0,
                          filename="assets/image/image_asteroids/planet1.png")

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

    def test_death_big_size(self):
        screen = pygame.display.set_mode((800, 450))
        generator = Generator(screen, 1000000000)
        null_vector = pygame.Vector2()
        test = Asteroid(generator=generator,
                        screen=screen,
                        start_position=pygame.Vector2(0, 0),
                        size=pygame.Vector2(60, 60),
                        direction=null_vector,
                        speed=0,
                        filename="assets/image/image_asteroids/planet1.png")

        test.death()
        self.assertTrue(len(generator.asteroids) == 2)

    def test_death_small_size(self):
        screen = pygame.display.set_mode((800, 450))
        generator = Generator(screen, 1000000000)
        null_vector = pygame.Vector2()
        test = Asteroid(generator=generator,
                        screen=screen,
                        start_position=pygame.Vector2(0, 0),
                        size=pygame.Vector2(50, 50),
                        direction=null_vector,
                        speed=0,
                        filename="assets/image/image_asteroids/planet1.png")

        test.death()
        self.assertTrue(len(generator.asteroids) == 0)
