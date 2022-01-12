from itertools import permutations 
import math


def solution():
    res = -1
    N = int(input())
    seq = list(permutations(list(map(int,input().split(" ")))))
    for value in seq:
        temp = 0
        for i in range(len(value)-1):
            temp +=abs(value[i]-value[i+1])
        res =  max(temp,res)
    print(res)
solution()