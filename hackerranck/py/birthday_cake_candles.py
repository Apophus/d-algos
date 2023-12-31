#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max_count = 1
    if len(candles) == max_count:
        return max_count

    frequency_map = Counter(candles)
    return frequency_map.most_common()[0][1]
    
if __name__ == "__main__":
    candles =  [3,1,2,3]  