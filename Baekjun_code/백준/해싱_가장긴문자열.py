#라빈 카프 알고리즘

# 문자를 해시화 하여 검출한다.
from re import sub
import sys

def mod(x):
    return x % 1234567891

# length = int(sys.stdin.readline().rstrip())
# input_str = sys.stdin.readline().strip()
length = 6
input_str = 'abcdef'

def solution(length, input_str):
    # 검출할 부분문자열의 길이
    for i in range(1,length+1):
        for j in range(length):
            if j<i:
                sub_str = input_str[j:i]
                print(sub_str)
            else:
                break

print(solution(length,input_str))