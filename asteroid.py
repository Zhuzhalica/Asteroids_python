from tracemalloc import start
import pygame


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen, start_position,  size, direction, speed, filename):
        """создаем астероид c стартовой позицией"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.speed = speed
        self.position = start_position
        self.screen_rect = screen.get_rect()
        image = pygame.image.load(filename)
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect(center =self.position)
        self.direction = direction
        

    
    def draw_asteroid(self):
        """отрисовка астероида"""
        self.screen.blit(self.image, self.position)

    
    def update(self):
        """Обновляем позицию астероида"""
        if self.InScreen:
            self.position += self.direction * self.speed
            self.draw_asteroid()
        else:
            self.kill()


    def InScreen(self):
        if self.rect.top > self.screen_rect.top or self.rect.bottom < self.screen_rect.bottom or self.rect.right > self.screen_rect.right or self.rect.left < self.screen_rect.left:
            return False
        return True