import pygame
import sys
from asteroid import Asteroid
from UFO import UFO
from space_ship import SpaceShip
import controls
from pygame.sprite import Group
from generator_asteroids import Generator
from menu import Menu
from Statistic import Stat


def run():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("Asteroids")
    space_ship = SpaceShip(screen)
    generator = Generator(screen, 15)
    asteroid = Asteroid(generator, screen, pygame.math.Vector2(100, 100),
                        pygame.math.Vector2(60, 60),
                        pygame.math.Vector2(1, 1), 1,
                        "assets/image/image_asteroids/default_asteroid.png")
    bullets = Group()
    menu = Menu(screen)
    all_sprites = Group()
    ufos = Group()
    all_sprites.add(space_ship)
    # for i in range(8):
    #     m = UFO(screen)
    #     all_sprites.add(m)
    #     ufos.add(m)
    stat = Stat(screen, space_ship)

    while True:
        if not menu.IsActive:
            controls.events(screen, space_ship, bullets)
            enemies = generator.asteroids.copy()
            enemies.add(ufos.copy())
            controls.interactions_controller(enemies, bullets,
                                             space_ship, stat)

            space_ship.update_ship()
            generator.update()
            asteroid.update()
            controls.screen_update(screen, space_ship, stat, generator,
                                   bullets, ufos)
            controls.update_bullets(bullets)
            controls.ufos_update(ufos)
            all_sprites.update()

            # all_sprites.draw(screen)
        else:
            menu.update()


run()
