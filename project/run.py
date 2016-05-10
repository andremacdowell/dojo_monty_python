# encoding: utf-8
import random

DAYS = range(1, 7)
FINE = DAYS + [1000]


def generate_sample(num_days=-1):
    if num_days == -1:
        num_days = random.choice(DAYS)
    input_num = range(1, num_days + 1)
    input_data = map(lambda x: (random.choice(DAYS), random.choice(FINE)),
                     input_num)
    return input_data


def rabbit_training(sample):
    current = (0, 0)
    stack = []
    fine = 0
    for rabbit in sample:
        stack.append([rabbit[0], rabbit[1]])
        if current[0] == 0:
            current = decide(stack)
            stack.remove(current)
        current[0] -= 1
        fine += calculate(stack)
    while(stack):
        if current[0] == 0:
            current = decide(stack)
            stack.remove(current)
        current[0] -= 1
        fine += calculate(stack)
    return fine


def decide(stack):
    best = stack[0]
    for rabbit in stack:
        if (float(rabbit[1]) / rabbit[0]) > (float(best[1]) / best[0]):
            best = rabbit
    return best


def calculate(stack):
    fine = 0
    for rabbit in stack:
        fine += rabbit[1]
    return fine

if __name__ == '__main__':
    sample = generate_sample()
    print "=== Entrada:"
    for rabbit in sample:
        print "{} {}".format(rabbit[0], rabbit[1])
    print "=== Saida:"
    print rabbit_training(sample)
