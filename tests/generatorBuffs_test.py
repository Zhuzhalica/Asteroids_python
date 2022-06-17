import unittest
import pygame
from space_ship import SpaceShip
from Buffs import Buff_Item, Buffs
from generator_buffs import Generator_Buffs
import time

screen = pygame.display.set_mode((800, 450))


class Space_Ship_Tests(unittest.TestCase):
    def test_empty_create(self):
        result = Generator_Buffs(screen=screen)
        self.assertEqual(str(result.screen), str(SpaceShip().screen))

    def test_make_buff(self):
        result = Generator_Buffs()
        result.make_buff()
        self.assertEqual(1, len(result.buffs))
        buff = result.buffs.sprites()[0]
        self.assertTrue(buff.enum_type in Buffs)

    def test_update(self):
        test = Generator_Buffs()

        self.assertEqual(test.count, 0)
        self.assertEqual(len(test.buffs), 0)
        test.update()
        self.assertEqual(test.count, 1)
        self.assertEqual(len(test.buffs), 0)
        test.update()
        self.assertEqual(test.count, 1)
        self.assertGreaterEqual(len(test.buffs), 0)
        test.update()
        self.assertEqual(test.count, 1)
        self.assertGreaterEqual(len(test.buffs), 0)
        self.assertLessEqual(len(test.buffs), 2)