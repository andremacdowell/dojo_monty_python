import random

DAYS = range(1, 8)
FINE = DAYS + [1000]


def generate_sample(num_days=7):
    input_num = range(random.randint(1, num_days + 1))
    input_data = map(lambda x: (DAYS[random.randint(0, len(DAYS) - 1)],
                                FINE[random.randint(0, len(FINE) - 1)]),
                     input_num)
    return input_data


def rabbit_training(sample):
    return 0

if __name__ == '__main__':
    print rabbit_training(generate_sample())
