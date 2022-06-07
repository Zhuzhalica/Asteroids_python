import pygame


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, screen):
        """создаем корабль"""
        pygame.sprite.Sprite.__init__(self)
        self.health = 50
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load("image/pixil-frame-0.png"),(50,50))

        # стартовая позиция
        self.screen_rect = screen.get_rect()
        self.position = pygame.math.Vector2(self.screen_rect.center)
        self.direction = pygame.math.Vector2(-1, 0)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        # переменные движения
        self.move_up = False
        self.turn_right = False
        self.turn_left = False
        self.speed = float(0)
        self.max_speed = 3
        self.acceleration = 0.05
        self.deceleration = 0.03
        self.angle = 0

    def draw_space_ship(self):
        """отрисовка корабля"""
        surf = pygame.transform.rotate(self.image, self.angle)
        position = surf.get_rect(center=self.position)
        self.screen.blit(surf, position)

    def update_ship(self):
        """обновление позиции корабля"""
        if self.move_up:
            self.speed = min(self.speed + self.acceleration, self.max_speed)
            self.position += self.direction * self.speed
        elif not self.move_up:
            self.speed = max(self.speed - self.deceleration, 0)
            self.position += self.direction * self.speed

        if self.health <= 0:
            self.kill()

        self.StayInScreen()

        if self.turn_right:
            self.direction.rotate_ip(1)
        if self.turn_left:
            self.direction.rotate_ip(-1)

        self.angle = (self.direction.angle_to((1, 0)) - 90) % 360
        self.rect.center = self.position

    def StayInScreen(self):
        if self.position.y < self.screen_rect.top:
            self.position.y += self.screen_rect.bottom - self.screen_rect.top

        if self.position.y > self.screen_rect.bottom:
            self.position.y -= self.screen_rect.bottom - self.screen_rect.top

        if self.position.x > self.screen_rect.right:
            self.position.x += self.screen_rect.left - self.screen_rect.right

        if self.position.x < self.screen_rect.left:
            self.position.x -= self.screen_rect.left - self.screen_rect.right

    def TakeDamage(self, damage):
        self.health -= damage
