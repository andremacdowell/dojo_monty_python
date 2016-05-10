# encoding:utf-8
import unittest
from project.run import (generate_sample, rabbit_training)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.sample = generate_sample()

    def test_single_day(self):
        self.sample = generate_sample(num_days=1)
        self.assertEqual(rabbit_training(self.sample), 0)

    def test_no_training(self):
        kwargs = {
            'num_days': 0
        }
        self.sample = generate_sample(**kwargs)
        self.assertEqual(rabbit_training(self.sample), 0)

    def test_two_rabbits(self):
        self.sample = generate_sample(num_days=2)
        fine = self.sample[1][1] * (self.sample[0][0] - 1)
        self.assertEqual(rabbit_training(self.sample), fine)
