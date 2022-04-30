import pygame


class SpaceShip:
    def __init__(self, screen):
        """создаем корабль"""

        self.screen = screen
        self.image = pygame.image.load("image/pixil-frame-0.png")

        # стартовая позиция
        self.screen_rect = screen.get_rect()
        self.position = pygame.math.Vector2(self.screen_rect.center)
        self.direction = pygame.math.Vector2(-1, 0)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        # объекты позиции (по сути - коллайдер)
        # self.centerx = float(self.rect.centerx)
        # self.centery = float(self.rect.centery)

        # переменные движения
        self.move_up = False
        self.turn_right = False
        self.turn_left = False
        self.speed = float(0)
        self.max_speed = 1

    def draw_space_ship(self):
        """отрисовка корабля"""
        self.screen.blit(self.image, self.position)

    def update_ship(self):
        """обновление позиции корабля"""
        if self.move_up and self.InScreen():
            self.speed = min(self.speed + 0.0005, self.max_speed)
            self.position += self.direction * self.speed
        elif not self.move_up and self.InScreen():
            self.speed = max(self.speed - 0.0005, 0)
            self.position += self.direction * self.speed

        if self.turn_right:
            self.direction.rotate_ip(0.1)
        if self.turn_left:
            self.direction.rotate_ip(-0.1)

        angle = self.direction.angle_to((1, 0))
        rotated_image = pygame.transform.rotate(self.image, angle - 90)
        self.screen.blit(rotated_image, rotated_image.get_rect(center=(round(self.position.x), round(self.position.y))))
        pygame.display.flip()
        self.rect.center = self.position

    def InScreen(self):
        return self.rect.top + self.direction.y * self.speed > self.screen_rect.top and \
               self.rect.bottom < self.screen_rect.bottom and \
               self.rect.left > self.screen_rect.left and \
               self.rect.right < self.screen_rect.right
