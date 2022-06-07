import pygame
import random

from asteroid import Asteroid


class Generator:
    def __init__(self, screen, frequency):
        self.screen = screen
        self.frequency = frequency
        self.asteroids = list()
        self.images = ("default_asteroid.png", "planet1.png", "planet2.png")
        self.count = 0

    def draw_asteroid(self):
        """Отрисовка всех астероидов"""
        for asteroid in self.asteroids:
            asteroid.draw_asteroid()

    def make_new_asteroid(self):
        start_position = (pygame.math.Vector2(-10, random.randint(-10, self.screen.get_rect().bottom)),
                          pygame.math.Vector2(self.screen.get_rect().right + 10,
                                              random.randint(-10, self.screen.get_rect().bottom)))

        direction = pygame.math.Vector2(random.uniform(-0.7, 0.7), random.uniform(-0.7, 0.7))
        size = pygame.math.Vector2(60, 60)
        speed = random.uniform(3, 5)
        image = "image/image_asteroids/" + random.choice(self.images)
        self.asteroids.append(Asteroid(self.screen, random.choice(start_position), size, direction, speed, image))

    def update(self):
        if self.count > self.frequency:
            self.make_new_asteroid()
            self.count = 0
        self.count += 1
        for asteroid in self.asteroids:
            asteroid.update()
