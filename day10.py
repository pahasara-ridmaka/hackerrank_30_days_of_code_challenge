#!/bin/python3

import math
import os
import random
import re
import sys

def to_binary(n: int):
    rem_arr = []
    #convert to binary
    binary = ''
    while(n>0):
        remainder = n%2
        n = n//2
        rem_arr.append(remainder)
        binary += str(remainder)

    binary_list = binary.split('0')
    max_len = 0
    for cluster in binary_list:
        if len(cluster) > max_len:
            max_len = len(cluster)
    

    # print(binary[::-1])
    print(max_len)
    

if __name__ == '__main__':
    n = int(input().strip())
    to_binary(n)
