"""
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

"""
from itertools import product

ADJACENT = {'1': '124', '2': '1235', '3': '236', '4': '1475', '5': '24568',
            '6': '3569', '7': '478', '8': '05789', '9': '689', '0': '08'}


def get_pins(observed):
    return [''.join(a) for a in product(*(ADJACENT[b] for b in observed))]

def get_pinsB(observed):
    if len(observed) == 1:
        return observed[0]
    return []
