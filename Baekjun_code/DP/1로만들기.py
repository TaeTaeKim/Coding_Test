##### Top_down방식--> 해당 값을 찾아가는 과정
import math
import sys
sys.setrecursionlimit(10**9)

dpvalue = {2:1,3:1,4:2}
n = int(input())

# def Topdown_solution(n):
#     if n==1: return 0

#     if n in dpvalue.keys():
#         return dpvalue[n]
#     else:
#         if n%3==0:
#             div3 = Topdown_solution(n//3)+1
#         else:
#             div3 = math.inf
        
#         if n%2==0:
#             div2 = Topdown_solution(n//2)+1
#         else:
#             div2 = math.inf
        
#         minus1 = Topdown_solution(n-1)+1

#         dpvalue[n] = min([div3,div2,minus1])
#         return dpvalue[n]

# print(Topdown_solution(n))


### Bottom up방식 --> 해당값을 만들어가는 과정.
def Bottomup_solution(n):
    if n==1: return 0
    if n in dpvalue.keys():
        return dpvalue[n]
    for i in range(5,n+1):
        if i%3==0:
            div3 = Bottomup_solution(i//3)+1
        else:
            div3 = math.inf
        
        if i%2==0:
            div2 = Bottomup_solution(i//2)+1
        else:
            div2 = math.inf
        
        minus1 = Bottomup_solution(i-1)+1

        dpvalue[i] = min([div3,div2,minus1])
    return dpvalue[i]
print(Bottomup_solution(n))