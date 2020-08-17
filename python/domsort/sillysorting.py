import random

from domsort import sortingutil


def bubble_sort(items):
    while not sortingutil.in_order(items):
        for i in range(len(items) - 1):
            if items[i] > items[i+1]:
                citem = items[i]
                items[i] = items[i+1]
                items[i+1] = citem
    return items

def bogo_sort(items):
    while not sortingutil.in_order(items):
        random.shuffle(items)
    return items

def stalin_sort(items):
    length = len(items)
    i = 1
    while i < length:
        if items[i] < items[i - 1]:
            items.pop(i)
            length -= 1
        else:
            i += 1
    return items