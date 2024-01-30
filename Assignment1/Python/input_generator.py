import random

def generate_int_list(length):
    random_list = []

    for i in range(0, 5):
        n = random.randint(1, 30)
        random_list.append(n)

    return random_list