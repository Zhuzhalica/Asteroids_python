import pygame
from Scripts.space_ship import SpaceShip
import Scripts.controls as controls
from pygame.sprite import Group
from Scripts.generator_asteroids import Generator
from Scripts.generator_buffs import Generator_Buffs
from Scripts.generator_UFO import Generator_UFO
from Scripts.statistic import Stat


class Game:
    def __init__(self, screen=pygame.display.set_mode((800, 450)),
                 player_name=''):
        """Создание игры"""
        self.screen = screen
        self.space_ship = SpaceShip(screen)
        self.generator_asteroids = Generator(screen, 20)
        self.generator_buffs = Generator_Buffs(screen, 200, 500)
        self.generator_UFO = Generator_UFO(self.space_ship, screen, 100, 200)
        self.bullets = Group()
        self.all_sprites = Group()
        self.all_sprites.add(self.space_ship)
        self.stat = Stat(screen, self.space_ship, player_name)
        self.game_over = False

    def game_update(self):
        """Обновление состояния и отрисовки объектов игры"""
        if self.space_ship.health > 0:
            controls.events(self.screen, self.space_ship, self.bullets)
            controls.interactions_controller(
                self.generator_asteroids.asteroids,
                self.generator_UFO.ufos, self.bullets,
                self.generator_UFO.bullets,
                self.generator_buffs.buffs,
                self.space_ship, self.stat)

            self.space_ship.update()
            self.generator_asteroids.update()
            self.generator_buffs.update()
            self.generator_UFO.update()

            controls.screen_update(self.screen, self.space_ship, self.stat,
                                   self.generator_asteroids.asteroids,
                                   self.generator_buffs.buffs, self.bullets,
                                   self.generator_UFO.bullets,
                                   self.generator_UFO.ufos)
            controls.update_bullets(self.bullets)
            controls.update_bullets(self.generator_UFO.bullets)
            self.all_sprites.update()
            # all_sprites.draw(screen)
        else:
            self.game_over = True
