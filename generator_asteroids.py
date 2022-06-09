import pygame
import random
from pygame.sprite import Group

from asteroid import Asteroid


class Generator:
    def __init__(self, screen, frequency):
        self.screen = screen
        self.frequency = frequency
        self.asteroids = Group()
        self.images = ("default_asteroid.png", "planet1.png", "planet2.png")
        self.count = 0

    def draw_asteroid(self):
        """Отрисовка всех астероидов"""
        for asteroid in self.asteroids:
            asteroid.draw_asteroid()

    def make_random_asteroid(self):
        start_position = (pygame.math.Vector2(-10, random.randint(-10, self.screen.get_rect().bottom)),
                          pygame.math.Vector2(self.screen.get_rect().right + 10,
                                              random.randint(-10, self.screen.get_rect().bottom)))

        direction = pygame.math.Vector2(random.uniform(-0.7, 0.7), random.uniform(-0.7, 0.7))
        size = random.uniform(0.6, 1.4) * 60
        size_v = pygame.math.Vector2(size, size)
        speed = random.uniform(3, 5)
        image = "assets/image/image_asteroids/" + random.choice(self.images)
        self.asteroids.add(Asteroid(self, self.screen, random.choice(start_position), size_v, direction, speed, image))

    def make_asteroid_with_size(self, position, size, image):
        start_position = position
        direction = pygame.math.Vector2(random.uniform(-0.7, 0.7), random.uniform(-0.7, 0.7))
        size_v = pygame.math.Vector2(size, size)
        speed = random.uniform(3, 5)
        self.asteroids.add(Asteroid(self, self.screen, start_position, size_v, direction, speed, image))

    def update(self):
        if self.count > self.frequency:
            self.make_random_asteroid()
            self.count = 0
        self.count += 1
        for asteroid in self.asteroids:
            asteroid.update()
