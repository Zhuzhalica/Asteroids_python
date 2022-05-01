import pygame
import sys
from bullet import Bullet


def events(screen, space_ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_event = event.pos
        #     for button in buttons:
        #         button.check(mouse_event)

        elif event.type == pygame.KEYDOWN:
            # перемещение
            if event.key == pygame.K_d:
                space_ship.turn_right = True

            if event.key == pygame.K_a:
                space_ship.turn_left = True

            if event.key == pygame.K_w:
                space_ship.move_up = True

            # стрельба
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, space_ship)
                new_bullet.shoot()
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                space_ship.move_up = False
            if event.key == pygame.K_d:
                space_ship.turn_right = False
            if event.key == pygame.K_a:
                space_ship.turn_left = False


def screen_update(bg_color, screen, space_ship, asteroid,  bullets):
    """обновление экрана"""
    #screen.fill(bg_color)
    image = pygame.image.load("image/cosmos.jpg")
    rect = screen.get_rect()
    redact_image = pygame.transform.scale(image, (rect.right - rect.left,rect.bottom - rect.top))
    screen.blit(redact_image, (0,0))
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # space_ship.draw_space_ship()
    asteroid.draw_asteroid()
    pygame.display.flip()
    


def update_bullets(bullets, space_ship):
    """обновление позиций пуль"""
    bullets.update(space_ship)

    # если пуля вышли за экран - удаляем ее
    for bullet in bullets.copy():
        if bullet.rect.left <= 0:
            bullet.remove()
