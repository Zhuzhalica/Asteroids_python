import pygame
import sys
from Scripts.bullet import Bullet
from Scripts.asteroid import Asteroid
import time


def events(screen, space_ship, bullets):
    """обработка пользовательских действий"""
    sound_shoot = pygame.mixer.Sound('sounds/shoot.mp3')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # начать перемещение
            if event.key == pygame.K_d:
                space_ship.turn_right = True

            if event.key == pygame.K_a:
                space_ship.turn_left = True

            if event.key == pygame.K_w:
                space_ship.move_up = True

            # стрельба
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, space_ship)
                sound_shoot.play(0)
                bullets.add(new_bullet)
                if space_ship.triple_gun:
                    bullet = Bullet(screen, space_ship, add_angle=15)
                    bullets.add(bullet)
                    bullet = Bullet(screen, space_ship, add_angle=-15)
                    bullets.add(bullet)

        elif event.type == pygame.KEYUP:
            # закончить перемещение
            if event.key == pygame.K_w:
                space_ship.move_up = False
            if event.key == pygame.K_d:
                space_ship.turn_right = False
            if event.key == pygame.K_a:
                space_ship.turn_left = False


def screen_update(screen, space_ship, stat, asteroids, buffs,
                  bullets, e_bullets, ufos):
    """обновление отрисовки экрана и объектов"""
    image = pygame.image.load("assets/image/cosmos.jpg")
    rect = screen.get_rect()
    redact_image = \
        pygame.transform.scale(image,
                               (rect.right - rect.left,
                                rect.bottom - rect.top))
    screen.blit(redact_image, (0, 0))

    for bullet in bullets.sprites():
        bullet.draw()

    for bullet in e_bullets.sprites():
        bullet.draw()

    for buff in buffs.sprites():
        buff.draw()

    for ufo in ufos:
        ufo.draw()

    for asteroid in asteroids.sprites():
        asteroid.draw()

    space_ship.draw_space_ship()
    stat.draw_stat()
    pygame.display.flip()


def update_bullets(bullets):
    """обновление позиций пуль"""
    bullets.update()
    # если пуля вышли за экран - удаляем ее
    for bullet in bullets.copy():
        if not bullet.in_screen():
            bullet.kill()


def interactions_controller(asteroids, ufos, bullets, e_bullets,
                            buffs, space_ship, stat):
    """Обработка взаимодействий объектов"""
    enemies = asteroids.copy()
    enemies.add(ufos.copy())


    # pygame.sprite.groupcollide(asteroids, ufos, True, True)
    # pygame.sprite.groupcollide(asteroids, e_bullets, True, True)
    collision_UP = pygame.sprite.spritecollideany(space_ship, e_bullets)

    collisions_BLE = pygame.sprite.groupcollide(bullets, enemies, True, True)
    collisions_PE = pygame.sprite.spritecollideany(space_ship, enemies)
    collisions_PBF = pygame.sprite.spritecollideany(space_ship, buffs)

    if time.perf_counter() - space_ship.start_time > 4:
        if collisions_PE:
            space_ship.take_damage()
            if type(collisions_PE) is Asteroid:
                collisions_PE.death()
            collisions_PE.kill()
        elif collision_UP:
            space_ship.take_damage()
            collision_UP.kill()

    if collisions_PBF:
        space_ship.get_buff(collisions_PBF)
        collisions_PBF.kill()



    for enemies_list in collisions_BLE.values():
        for enemy in enemies_list:
            stat.make_stat(enemy)
