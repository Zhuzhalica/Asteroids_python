import pygame
import sys

from UFO import UFO
from bullet import Bullet
from asteroid import Asteroid


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
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                space_ship.move_up = False
            if event.key == pygame.K_d:
                space_ship.turn_right = False
            if event.key == pygame.K_a:
                space_ship.turn_left = False


def screen_update(screen, space_ship, stat, asteroid, bullets, ufos):
    """обновление экрана"""
    image = pygame.image.load("assets/image/cosmos.jpg")
    rect = screen.get_rect()
    redact_image = pygame.transform.scale(image, (rect.right - rect.left, rect.bottom - rect.top))
    screen.blit(redact_image, (0, 0))

    for bullet in bullets.sprites():
        bullet.draw()

    for ufo in ufos:
        ufo.draw()

    space_ship.draw_space_ship()
    asteroid.draw_asteroid()
    stat.draw_stat()
    pygame.display.flip()


def update_bullets(bullets):
    """обновление позиций пуль"""
    bullets.update()
    # если пуля вышли за экран - удаляем ее
    for bullet in bullets.copy():
        if not bullet.in_screen():
            bullet.kill()


def ufos_update(ufos):
    ufos.update()


def interactions_controller(enemies, bullets, space_ship, stat):
    collisions_with_bullet = pygame.sprite.groupcollide(bullets, enemies, True, True)
    collisions_with_player = pygame.sprite.spritecollideany(space_ship, enemies)

    if collisions_with_player:
        space_ship.take_damage()
        if type(collisions_with_player) is Asteroid:
            collisions_with_player.death()
        collisions_with_player.kill()

    for enemies_list in collisions_with_bullet.values():
        for enemy in enemies_list:
            if type(enemy) is Asteroid:
                stat.score += int(100 * (enemy.image.get_size()[0] / 84))
                enemy.death()
            elif type(enemy) is UFO:
                stat.score += int(200 * (enemy.image.get_size()[0] / 60))
                enemy.kill()