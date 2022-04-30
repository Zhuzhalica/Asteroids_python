import pygame
import sys
from space_ship import SpaceShip
import controls
from pygame.sprite import Group
from menu import Menu

def run():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Asteroids")
    bg_color = (0, 0, 0)
    space_ship = SpaceShip(screen)
    bullets = Group()
    font = pygame.font.SysFont(None, 36)
    menu = Menu(screen, font)

    while True:
        # if not menu.IsActive:
        controls.events(screen, space_ship, bullets)
        space_ship.update_ship()
        controls.screen_update(bg_color, screen, space_ship, bullets)
        controls.update_bullets(bullets, space_ship)
        # else:
        #     menu.update()

run()
