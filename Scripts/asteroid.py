import pygame
import Scripts.game_manager as game_manager


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, generator=None,
                 screen=pygame.display.set_mode((800, 450)),
                 start_position=pygame.Vector2(), size=pygame.Vector2(),
                 direction=pygame.Vector2(), speed=0,
                 filename="assets/image/image_asteroids/planet1.png"):
        """создание астероида"""
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
        self.rect.width = int(self.rect.width * 0.9)
        self.rect.height = int(self.rect.height * 0.9)
        self.direction = direction
        self.max_size = 84

    def draw(self):
        """отрисовка астероида"""
        self.screen.blit(self.image, self.position)

    def update(self):
        """Обновляем позицию астероида"""
        self.position += self.direction * self.speed
        self.rect.center = self.position

    def in_screen(self):
        """находится ли астероид в границах экрана"""
        return game_manager.in_screen(self.screen, self.position)

    def death(self):
        """разрушение астероида и создание его обломков"""
        if self.image.get_size()[0] > 55:
            for i in range(2):
                self.generator. \
                    make_asteroid_with_size(self.position.copy(),
                                            self.image.get_size()[0] - 20,
                                            self.image_file)
