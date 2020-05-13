#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    mag_dict = {}

    for word in magazine:
        if word not in mag_dict:
            mag_dict[word] = 1
        else:
            mag_dict[word] += 1
    
    note_dict = {}

    for word in note:
        if word not in note_dict:
            note_dict[word] = 1
        else:
            note_dict[word] += 1

    checked_words = 0

    for word in note_dict:
        if word not in mag_dict:
            return False
        elif word in mag_dict and mag_dict[word] < note_dict[word]:
            return False
    
    return True


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    answer = checkMagazine(magazine, note)
    if answer:
        print("Yes")
    else:
        print("No")