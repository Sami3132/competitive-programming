#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    newArr = []
    for query in queries:
        newArr.append([query[0], query[2], 1])
        newArr.append([query[1] + 1, query[2], -1])
    
    newArr.sort(key=lambda x: (x[0], x[2]))
    
    ans = 0
    total = 0
    
    for el in newArr:
        if el[2] == 1:
            total += el[1]
        else:
            total -= el[1]
        
        ans = max(ans, total)
        
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
