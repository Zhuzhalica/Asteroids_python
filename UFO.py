import random
import pygame
from bullet import Bullet


class UFO(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.sound_shoot = pygame.mixer.Sound('sounds/shoot.mp3')
        """создаем астероид c стартовой позицией"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.health = 100
        self.image = pygame.transform.scale(pygame.image.load("assets/image/ufo.png"), (60, 40))
        self.direction = pygame.math.Vector2(random.uniform(-0.7, 0.7), random.uniform(-0.7, 0.7))
        self.angle = self.direction.angle_to((1, 0))+ 40
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen.get_rect().width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 4)

    def update(self):
        self.rect.center += self.speed * self.direction
        self.stay_in_screen()
        if self.health <= 0:
            self.kill()


    def stay_in_screen(self):
        """Если игрок выходит за границы экарана, то оказывается с другой его стороны"""
        if self.rect.y < self.screen_rect.top:
            self.rect.y += self.screen_rect.bottom - self.screen_rect.top

        if self.rect.y > self.screen_rect.bottom:
            self.rect.y -= self.screen_rect.bottom - self.screen_rect.top

        if self.rect.x > self.screen_rect.right:
            self.rect.x += self.screen_rect.left - self.screen_rect.right

        if self.rect.x < self.screen_rect.left:
            self.rect.x -= self.screen_rect.left - self.screen_rect.right


    def in_screen(self):
        if self.rect.top > self.screen_rect.top\
                or self.rect.bottom < self.screen_rect.bottom\
                or self.rect.right > self.screen_rect.right\
                or self.rect.left < self.screen_rect.left:
            return False
        return True


    def draw(self):
        """отрисовка астероида"""
        self.screen.blit(self.image, self.rect)

    
    def shoot(self):
        self.sound_shoot.play(0)
        bullet = Bullet(self.screen, self)
        self.bullets.add(bullet)

