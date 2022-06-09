import random
import pygame


class UFO(pygame.sprite.Sprite):
    def __init__(self, screen):
        """создаем астероид c стартовой позицией"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.health = 100
        self.image = pygame.transform.scale(pygame.image.load("assets/image/ufo.png"), (60, 40))
        self.direction = pygame.math.Vector2(random.uniform(-0.7, 0.7), random.uniform(-0.7, 0.7))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen.get_rect().width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(2, 8)

    def update(self):
        self.rect.center += self.speed * self.direction
        if self.rect.top > self.screen.get_rect().height:
            self.rect.y = -5
        if self.rect.bottom < self.screen.get_rect().top:
            self.rect.y = self.screen.get_rect().height
        if self.rect.left > self.screen.get_rect().width:
            self.rect.y = -5
        if self.rect.right < self.screen.get_rect().left:
            self.rect.x = self.screen.get_rect().width
        if self.health <= 0:
            self.kill()

    def InScreen(self):
        if self.rect.top > self.screen_rect.top or self.rect.bottom < self.screen_rect.bottom or self.rect.right > self.screen_rect.right or self.rect.left < self.screen_rect.left:
            return False
        return True

    def draw(self):
        """отрисовка астероида"""
        self.screen.blit(self.image, self.rect)
