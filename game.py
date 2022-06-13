import pygame
import sys
from asteroid import Asteroid
from UFO import UFO
from space_ship import SpaceShip
import controls
from pygame.sprite import Group
from generator_asteroids import Generator
from menu import Menu
from statistic import Stat


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.space_ship = SpaceShip(screen)
        self.generator = Generator(screen, 15)
        self.asteroid = Asteroid(self.generator, screen, pygame.math.Vector2(100, 100),
                                 pygame.math.Vector2(60, 60),
                                 pygame.math.Vector2(1, 1), 1,
                                 "assets/image/image_asteroids/default_asteroid.png")
        self.bullets = Group()
        self.all_sprites = Group()
        self.ufos = Group()
        self.all_sprites.add(self.space_ship)
        for i in range(8):
            m = UFO(screen)
            self.all_sprites.add(m)
            self.ufos.add(m)
        self.stat = Stat(screen, self.space_ship)
        self.game_over = False

    def game_update(self):
        if self.space_ship.health > 0:
            controls.events(self.screen, self.space_ship, self.bullets)
            enemies = self.generator.asteroids.copy()
            enemies.add(self.ufos.copy())
            controls.interactions_controller(enemies, self.bullets,
                                             self.space_ship, self.stat)
            self.space_ship.update_ship()
            self.generator.update()
            self.asteroid.update()

            controls.screen_update(self.screen, self.space_ship, self.stat, self.generator,
                                   self.bullets, self.ufos)
            controls.update_bullets(self.bullets)
            controls.ufos_update(self.ufos)
            self.all_sprites.update()
            # all_sprites.draw(screen)
        else:
            self.game_over = True
