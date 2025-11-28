#!/bin/python3

import math
import os
import random
import re
import sys

def is_even(n: int):
    remainder = n%2
    
    if remainder == 0:
        status = True
    else:
        status = False
        
    return status
    
def check_range(n: int):
    weird = "Weird"
    nt_weird = "Not Weird"
    if is_even(n):
        if (n>=2 and n<=5):
            print(nt_weird)
        elif (n>=6 and n<=20):
            print(weird)
        elif (n>=20):
            print(nt_weird)
    else:
        print(weird)
    
if __name__ == '__main__':
    N = int(input().strip())
    check_range(N)
