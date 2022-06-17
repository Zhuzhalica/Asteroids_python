import unittest
import pygame
from generator_asteroids import Generator

screen = pygame.display.set_mode((800, 450))


class Generator_Asteroid_Tests(unittest.TestCase):
    def test_empty_create(self):
        result = Generator(screen, frequency=0)
        self.assertEqual(str(result.__dict__), str(Generator().__dict__))

    def test_random_asteroid(self):
        result = Generator(screen, frequency=5)
        result.make_random_asteroid()
        self.assertEqual(len(result.asteroids), 1)

    def test_size_asteroid(self):
        null_vector = pygame.Vector2()
        result = Generator(screen, frequency=5)
        result.make_asteroid_with_size(position=null_vector,
                                       size=null_vector,
                                       image="assets/image/"
                                             "image_asteroids/planet1.png")
        self.assertEqual(len(result.asteroids), 1)

    def test_update_count(self):
        screen = pygame.display.set_mode((4000, 4000))
        test = Generator(screen, frequency=0)

        self.assertEqual(test.count, 0)
        self.assertEqual(len(test.asteroids), 0)
        test.update()
        self.assertEqual(test.count, 1)
        self.assertEqual(len(test.asteroids), 0)
        test.update()
        self.assertEqual(test.count, 1)
        self.assertGreaterEqual(len(test.asteroids), 0)
        test.update()
        self.assertEqual(test.count, 1)
        self.assertGreaterEqual(len(test.asteroids), 0)
        self.assertLessEqual(len(test.asteroids), 2)

    def test_update_kill_asteroid(self):
        screen = pygame.display.set_mode((4000, 4000))
        test = Generator(screen, frequency=42)
        test.make_asteroid_with_size(position=pygame.Vector2(2000, 2000),
                                     size=pygame.Vector2(1, 1),
                                     image="assets/image/"
                                           "image_asteroids/planet1.png")
        test.make_asteroid_with_size(position=pygame.Vector2(4200, 4200),
                                     size=pygame.Vector2(1, 1),
                                     image="assets/image/"
                                           "image_asteroids/planet1.png")
        test.update()

        self.assertEqual(1, len(test.asteroids))
