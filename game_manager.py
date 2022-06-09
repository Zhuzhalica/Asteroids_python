import pygame


def in_screen(screen, pos):
    screen_rect = screen.get_rect()
    return screen_rect.top < pos.y < screen_rect.bottom and screen_rect.left < pos.x < screen_rect.right
