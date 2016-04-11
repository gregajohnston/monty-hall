from nose.tools import raises

from monty_hall import *
# from random import *


def test_set_doors():
    assert set_doors(3) in [[0,0,1], [0,1,0], [1,0,0]]

def test_reveal_bad_door():
    assert reveal_bad_door(0, [1,0,0]) == [0, -1, 1] or [0, 1, -1]

def test_change_doors_or_not():
    assert change_doors_or_not(1, 0, [0,-1,1]) == (2, [0,-1,1])

def test_win_or_lose():
    assert win_or_lose(2, [0,-1,1]) == 1
