import unittest
from monster import Monster
import pygame


class Test(unittest.TestCase):
    def setUp(self):
        self.pos_x_zero = 0
        self.pos_x_over_pos = 1500
        self.pos_x_over_neg = -1000
        self.pos_x_limit_pos = 1400
        self.pos_x_limit_neg = -100
        self.monster1 = Monster(pygame.sprite.Sprite)
        self.value_x = [-1000, -100, 0, 100, 1400, 1500]
        print(self.monster1.rect.x)
        self.monster1.rect.x = -200
        self.monster1.forward()
        print(self.monster1.rect.x)


    def tearDown(self):
        pass

    """def test_forward(self):
        for value in self.value_x:
            print(value)
            self.monster1.rect.x = value
            self.monster1.forward()
            if value < -100:
                self.assertEqual(self.monster1.rect.x, -100)
            elif -100 <= value <= 1400:
                self.assertEqual(self.monster1.rect.x, value)
            elif value > 1400:
                self.assertEqual(self.monster1.rect.x, 1400)"""


if __name__ == '__main__':
    unittest.main()
