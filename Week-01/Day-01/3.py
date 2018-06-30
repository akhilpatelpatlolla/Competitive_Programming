import unittest
import sys
def highest_product_of_3(arr):
    n=len(arr)
    if (n < 3):
        raise ValueError("error!")
    maxA = -float('inf')
    maxB = -float('inf')
    maxC = -float('inf')
    minA = sys.maxsize
    minB = sys.maxsize
 
    for i in range(n):
        if (arr[i] > maxA):
            maxC = maxB
            maxB = maxA
            maxA = arr[i]
        elif (arr[i] > maxB):
            maxC = maxB
            maxB = arr[i]
        elif (arr[i] > maxC):
            maxC = arr[i] 
        if (arr[i] < minA):
            minB = minA
            minA = arr[i] 
        elif(arr[i] < minB):
            minB = arr[i]
    return max(minA * minB * maxA,maxA * maxB * maxC)
actual = highest_product_of_3([int(x) for x in input().split(",")])
print(actual)