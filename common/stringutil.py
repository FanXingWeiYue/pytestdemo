import random


def random_string(number):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(number):
        sa.append(random.choice(seed))
    result = ''.join(sa)
    return result

