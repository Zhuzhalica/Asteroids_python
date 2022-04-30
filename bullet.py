import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, space_ship):
        """иницилизация пули"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = (255, 255, 255)
        self.speed = 1
        self.position = space_ship.position
        self.direction = space_ship.direction
        self.rect.center = space_ship.position
        self.rect.center = self.position + space_ship.direction * 10
        self.y = float(self.rect.y)
        self.direction_shoot = pygame.math.Vector2(0, 0)

    def shoot(self):
        self.position += self.direction * self.speed
        self.direction_shoot = self.direction

    def update(self, space_ship):
        """Обновляем позицию пули"""
        self.rect.center = self.position + self.direction * 50
        self.position = space_ship.position

    def draw_bullet(self):
        """Отрисовываем пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)
