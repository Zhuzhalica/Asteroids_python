import random
import pygame
from Scripts.bullet import Bullet


class UFO(pygame.sprite.Sprite):
    def __init__(self, player, bullets,
                 screen=pygame.display.set_mode((800, 450)),
                 position=pygame.Vector2(0, 0)):
        """создаем НЛО cо стартовой позицией"""
        self.sound_shoot = pygame.mixer.Sound('sounds/shoot.mp3')
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.count_frames = random.randrange(20, 40)
        self.count_fr_move = 0
        self.image = pygame.transform.scale(
            pygame.image.load("assets/image/ufo.png"), (60, 40))
        self.direction = pygame.math.Vector2(
            random.uniform(-0.7, 0.7), random.uniform(-0.7, 0.7))
        self.angle_turn = 80

        self.target = player
        self.bullets = bullets
        self.frequency_bullets = random.randint(100, 300)
        self.count_frames_bullet = 0

        self.angle = self.direction.angle_to((1, 0)) + 40
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.center = self.position
        self.max_size = 60
        self.speed = random.randrange(3, 4)

    def update(self):
        """Обновление позиции НЛО"""
        self.position += self.speed * self.direction
        self.rect.center = self.position
        self.move_zigzag()
        self.stay_in_screen()

        if self.count_frames_bullet > self.frequency_bullets:
            self.shoot()
            self.count_frames_bullet = 0
        self.count_frames_bullet += 1

    def stay_in_screen(self):
        """Если НЛО выходит за границы экарана,
         то оказывается с другой его стороны"""
        if self.position.y <= self.screen_rect.top:
            self.position.y += self.screen_rect.bottom - self.screen_rect.top

        if self.position.y >= self.screen_rect.bottom:
            self.position.y -= self.screen_rect.bottom - self.screen_rect.top

        if self.position.x >= self.screen_rect.right:
            self.position.x += self.screen_rect.left - self.screen_rect.right

        if self.position.x <= self.screen_rect.left:
            self.position.x -= self.screen_rect.left - self.screen_rect.right

    def draw(self):
        """отрисовка НЛО"""
        self.screen.blit(self.image, self.rect)

    def shoot(self):
        """Стрельба НЛО"""
        self.sound_shoot.play(0)
        bullet = Bullet(self.screen, self)
        self.bullets.add(bullet)

    def move_zigzag(self):
        """Движение НЛО по зиг-загу"""
        if self.count_fr_move < self.count_frames:
            self.count_fr_move += 1
        if self.count_fr_move >= self.count_frames:
            self.direction = pygame.math.Vector2.rotate(
                self.direction, self.angle_turn)
            self.angle_turn *= - 1
            self.count_fr_move = 0
