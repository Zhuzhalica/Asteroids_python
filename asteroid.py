from tracemalloc import start
import pygame

import game_manager


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, generator, screen, start_position, size, direction, speed, filename):
        """создаем астероид c стартовой позицией"""
        pygame.sprite.Sprite.__init__(self)
        self.generator = generator
        self.screen = screen
        self.speed = speed
        self.position = start_position
        self.screen_rect = screen.get_rect()
        self.image_file = filename
        image = pygame.image.load(filename)
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect(center=self.position)
        self.rect.width = int(self.rect.width * 0.82)
        self.rect.height = int(self.rect.height * 0.82)
        self.direction = direction

    def draw_asteroid(self):
        """отрисовка астероида"""
        self.screen.blit(self.image, self.position)

    def update(self):
        """Обновляем позицию астероида"""
        if self.in_screen:
            self.position += self.direction * self.speed
            self.rect.center = self.position
            self.draw_asteroid()
        else:
            self.kill()

    def in_screen(self):
        return game_manager.in_screen(self.screen, self.position)

    def death(self):
        if self.image.get_size()[0] > 55:
            self.generator.make_asteroid_with_size(self.position.copy(), self.image.get_size()[0] - 20, self.image_file)
            self.generator.make_asteroid_with_size(self.position.copy(), self.image.get_size()[0] - 20, self.image_file)
