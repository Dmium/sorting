import random


def in_order(items):
    for i in range(len(items) - 1):
        if items[i] > items[i+1]:
            return False
    return True

def generate_random_list(length):
    generated_list = []
    for _ in range(length):
        generated_list.append(random.randint(-127, 127))
    return(generated_list)
