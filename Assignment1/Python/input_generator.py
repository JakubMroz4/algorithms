import random

def generate_int_list(length):
    random_list = []

    for i in range(0, length):
        n = random.randint(1, 1_000_000)
        random_list.append(n)

    return random_list