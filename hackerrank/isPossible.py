#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isPossible' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#  4. INTEGER d
#

def isPossible(a, b, c, d):
    if a == c and b == d:
        return 'Yes'
    if a + b <= c and isPossible(a + b, b, c, d) == 'Yes':
        return 'Yes'
    if b + a <= d and isPossible(a, a + b, c, d) == 'Yes':
        return 'Yes'
    return 'No'


def isPossible(sx, sy, tx, ty):
    # Imagine you're at a starting point on a grid, and you want to reach another point on the same grid. You can only move in two ways: either left or down. The question is, can you reach your destination using only these moves?
    # We start a loop that continues as long as two conditions are true: (1) tx is greater than or equal to sx, and (2) ty is greater than or equal to sy. These conditions mean we can still make moves.
    while (tx >= sx and ty >= sy):
        # check if we have reached ends
        # If tx becomes equal to sx, it means we can't move left anymore. In this case, we check if the difference between ty and sy (how far we need to go down) is divisible by tx (how many steps we can take down at once). If it's divisible (no remainder), we can reach the destination, so we return "yes" (True).
        if tx == sx:
            return (ty-sy) % tx == 0
        # Similarly, if ty becomes equal to sy, it means we can't move down anymore. We check if the difference between tx and sx (how far we need to go left) is divisible by ty (how many steps we can take left at once). If it's divisible (no remainder), we can reach the destination, so we return "yes" (True).
        if ty == sy:
            return (tx-sx) % ty == 0

        # step
        if ty > tx:
            ty = ty % tx
        else:
            tx = tx % ty
    # If we haven't reached either of the "can't move anymore" situations, we decide on one of two moves:

    # If ty is greater than tx, we move down. We do this by finding out how many steps we can take down at once (ty % tx), and we update ty to that value.
    # If tx is greater than or equal to ty, we move left. We find out how many steps we can take left at once (tx % ty), and we update tx to that value.
    # We keep repeating these moves until one of the "can't move anymore" situations is reached.
    return False
