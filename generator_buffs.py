import pygame
import random
from pygame.sprite import Group

from asteroid import Asteroid


class Generator_Buffs:
    def __init__(self, screen, frequency):
        self.screen = screen
        self.frequency = frequency
        self.asteroids = Group()
        self.images = ("assets/image/space-ship-protected.png")
        self.count = 0

    def draw_asteroid(self):
        """Отрисовка всех астероидов"""
        for asteroid in self.asteroids:
            asteroid.draw_asteroid()

    def make_random_buffs(self):
        x = random.randint(0, self.screen.get_rect().width)
        y = random.randint(0, self.screen.get_rect().height)
        position = pygame.Vector2(x, y)

        size = random.uniform(0.6, 1.4) * 60
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