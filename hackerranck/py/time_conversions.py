#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    split_time = s.split(':')
    print(split_time)
    hour, minute, seconds = split_time[0], split_time[1], split_time[2]
    if int(hour) < 12:
        if 'pm' in s.lower():
            return f"{int(hour)+12}:{minute}:{seconds.replace('PM','')}"   
        return f"{hour}:{minute}:{seconds.replace('AM','')}"
    if 'pm' in s.lower():
        return f"12:{minute}:{seconds.replace('PM','')}"
    return f"00:{minute}:{seconds.replace('AM','')}"

if __name__ == '__main__':
    s = '12:45:54PM' 
    print(timeConversion(s))