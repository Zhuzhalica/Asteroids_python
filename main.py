import pygame
import sys
from asteroid import Asteroid
from space_ship import SpaceShip
import controls
from pygame.sprite import Group
from generator_asteroids import Generator
from menu import Menu


def run():
    image = pygame.image.load("image\cosmos.jpg")
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Asteroids")
    bg_color = (0, 0, 0)
    space_ship = SpaceShip(screen)
    generator = Generator(screen, 8)
    asteroid = Asteroid(screen, pygame.math.Vector2(100, 100), pygame.math.Vector2(60, 60), pygame.math.Vector2(1, 1), 1, "image/image_asteroids/default_asteroid.png")
    bullets = Group()
    font = pygame.font.SysFont(None, 36)
    menu = Menu(screen)
    all_sprites = pygame.sprite.Group()
    
    while True:
        if not menu.IsActive:
            controls.events(screen, space_ship, bullets)
            space_ship.update_ship()
            generator.update()
            asteroid.update()
            all_sprites.update()

            controls.screen_update(bg_color, screen, space_ship, generator, bullets)
            controls.update_bullets(bullets, space_ship)
        else:
            menu.update()
            
        

run()
