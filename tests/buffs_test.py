import unittest
import pygame
from Scripts.Buffs import Buff_Item, Buffs

screen = pygame.display.set_mode((800, 450))


class Buffs_Tests(unittest.TestCase):
    def test_incorrect_create(self):
        with self.assertRaises(ValueError) as e:
            Buff_Item('ssss')

        self.assertEqual("ssss doesn`t exist in Buffs",
                         e.exception.args[0])

    def test_create(self):
        test = Buff_Item(Buffs.Shield)
        image = pygame.transform.scale(
            pygame.image.load("assets/image/space-ship-pr.png"),
            (30, 30))
        self.assertEqual(str(image), str(test.image))
        self.assertEqual(Buffs.Shield, test.enum_type)
