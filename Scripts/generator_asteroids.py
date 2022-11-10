import pygame
import random
from pygame.sprite import Group

from Scripts.asteroid import Asteroid


class Generator:
    def __init__(self, screen=pygame.display.set_mode((800, 450)),
                 frequency=0):
        """Создание генератора астероидов"""
        self.screen = screen
        self.frequency = frequency
        self.asteroids = Group()
        self.images = ("default_asteroid.png", "planet1.png",
                       "planet2.png")
        self.count = 0

    def draw_asteroid(self):
        """Отрисовка всех астероидов"""
        for asteroid in self.asteroids:
            asteroid.draw_asteroid()

    def make_random_asteroid(self):
        """Создание случайного астероида"""
        start_position = (
            pygame.math.Vector2(0,
                                random.
                                randint(0,
                                        self.screen.get_rect().bottom)),
            pygame.math.Vector2(self.screen.get_rect().right,
                                random.
                                randint(0,
                                        self.screen.get_rect().bottom)))

        direction = pygame.math.Vector2(random.uniform(-0.7, 0.7),
                                        random.uniform(-0.7, 0.7))
        size = random.uniform(0.6, 1.4) * 60
        size_v = pygame.math.Vector2(size, size)
        speed = random.uniform(5, 8)
        image = "assets/image/image_asteroids/" +\
                random.choice(self.images)
        self.asteroids.add(Asteroid(self, self.screen,
                                    random.choice(start_position),
                                    size_v, direction, speed, image))

    def make_asteroid_with_size(self, position, size, image):
        """Создание астероида по характеристикам"""
        direction = pygame.math.Vector2(random.uniform(-0.7, 0.7),
                                        random.uniform(-0.7, 0.7))
        size_v = pygame.math.Vector2(size, size)
        speed = random.uniform(5, 8)
        self.asteroids.add(Asteroid(self, self.screen, position,
                                    size_v, direction, speed, image))

    def update(self):
        """Обновление генератора астероидов и самих астероидов"""
        if self.count > self.frequency:
            self.make_random_asteroid()
            self.count = 0
        self.count += 1

        self.asteroids.update()
        for asteroid in self.asteroids:
            if not asteroid.in_screen():
                asteroid.kill()
