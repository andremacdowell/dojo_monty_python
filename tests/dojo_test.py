import unittest
import random

days = range(1, 8)
fine = days + [1000]

MAX_DAYS = 7


def _generate_random_input():
    input_num = range(random.randint(1, MAX_DAYS + 1))
    input_data = map(lambda x: (days[random.randint(0, len(days) - 1)],
                                fine[random.randint(0, len(fine) - 1)]),
                     input_num)
    return input_data


class TestCase(unittest.TestCase):
    def setUp(self):
        self.input_data = _generate_random_input()

    def test(self):
        pass
