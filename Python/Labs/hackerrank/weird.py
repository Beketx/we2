#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())

if((n%2==0 and n>20) or (n%2==0 and n in range(2,5))):
    print("Not Weird")
elif(n % 2 != 0 or (n % 2 == 0 and n in range(6,20))):
    print("Weird")
else:
    print("Weird")

