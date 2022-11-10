import unittest
import pygame
from Scripts.space_ship import SpaceShip
from Scripts.Buffs import Buff_Item, Buffs
import time

screen = pygame.display.set_mode((800, 450))


class Space_Ship_Tests(unittest.TestCase):
    def test_empty_create(self):
        result = SpaceShip(screen)
        self.assertEqual(str(result.screen), str(SpaceShip().screen))

    def test_update_position(self):
        screen = pygame.display.set_mode((800, 450))
        test = SpaceShip(screen)
        test.move_up = True
        for i in range(10):
            test.update()
        self.assertAlmostEqual(test.acceleration * 10,
                               test.speed, delta=1e-5)
        self.assertAlmostEqual(398.35, test.position.x, delta=1e-5)
        self.assertAlmostEqual(225, test.position.y, delta=1e-5)

        test.move_up = False
        for i in range(10):
            test.update()
        self.assertAlmostEqual(0.15, test.speed, delta=1e-5)
        self.assertAlmostEqual(396.175, test.position.x, delta=1e-5)
        self.assertAlmostEqual(225, test.position.y, delta=1e-5)

    def test_update_speed(self):
        screen = pygame.display.set_mode((800, 450))
        test = SpaceShip(screen)
        test.move_up = True
        for i in range(int(test.max_speed / test.acceleration) + 5):
            test.update()
        self.assertAlmostEqual(test.max_speed, test.speed, delta=1e-5)

        test.move_up = False
        for i in range(int(test.max_speed / test.deceleration) + 5):
            test.update()
        self.assertAlmostEqual(0, test.speed, delta=1e-5)

    def test_update_turn(self):
        test = SpaceShip(screen)
        test.turn_right = True
        for i in range(9):
            test.update()

        self.assertEqual(72, test.angle)
        self.assertEqual(pygame.Vector2(-0.951057, -0.309017),
                         test.direction)

        test.turn_right = False
        test.turn_left = True
        test.direction = pygame.math.Vector2(-1, 0)
        test.angle = 0
        for i in range(4):
            test.update()

        self.assertEqual(98, test.angle)
        self.assertEqual(pygame.Vector2(-0.990268, 0.139173),
                         test.direction)

    def test_stay_in_screen(self):
        screen = pygame.display.set_mode((10, 10))
        test = SpaceShip(screen)

        test.position = pygame.Vector2(15, 5)
        result_position = pygame.Vector2(5, 5)
        test.stay_in_screen()
        self.assertEqual(test.position, result_position)

        test.position = pygame.Vector2(-5, 5)
        result_position = pygame.Vector2(5, 5)
        test.stay_in_screen()
        self.assertEqual(test.position, result_position)

        test.position = pygame.Vector2(5, 15)
        result_position = pygame.Vector2(5, 5)
        test.stay_in_screen()
        self.assertEqual(test.position, result_position)

        test.position = pygame.Vector2(5, -5)
        result_position = pygame.Vector2(5, 5)
        test.stay_in_screen()
        self.assertEqual(test.position, result_position)

    def test_take_damage(self):
        screen.get_rect()
        result = SpaceShip()
        result.health -= 1
        test = SpaceShip()
        test.take_damage()
        self.assertEqual(result.health, test.health)

    def test_buff_shield(self):
        test = SpaceShip()
        item = Buff_Item(enum=Buffs.Shield)
        test.get_buff(item)
        image = \
            pygame.transform.scale(pygame.image.load
                                   ("assets/image/space-ship-pr.png"),
                                   (50, 50))
        self.assertTrue(test.has_shield)
        self.assertEqual(str(image), str(test.image))

        test.take_damage()
        image = \
            pygame.transform.scale(pygame.image.load
                                   ("assets/image/space-ship.png"),
                                   (50, 50))
        self.assertFalse(test.has_shield)
        self.assertEqual(3, test.health)
        self.assertEqual(str(image), str(test.image))

    def test_buff_health(self):
        test = SpaceShip()
        item = Buff_Item(enum=Buffs.HP)
        test.get_buff(item)
        self.assertEqual(4, test.health)

    def test_triple_gun(self):
        test = SpaceShip()
        item = Buff_Item(enum=Buffs.Triple_Gun)
        time_test = test.start_triple_gun
        test.get_buff(item)
        self.assertTrue(test.triple_gun)
        self.assertNotEqual(time_test, test.start_triple_gun)
        while time.perf_counter() - test.start_triple_gun < 8.5:
            pass
        test.update()
        self.assertFalse(test.triple_gun)

    def test_incorrect_buff(self):
        with self.assertRaises(ValueError) as e:
            test = SpaceShip()
            test.get_buff("saddsa")

        self.assertEqual("Buff /saddsa/ doesn`t exist or"
                         " doesn`t have attribute enum_type",
                         e.exception.args[0])
