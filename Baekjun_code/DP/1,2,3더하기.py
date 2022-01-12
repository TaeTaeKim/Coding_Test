testcase = int(input())
dpvalue = {1:1,2:2,3:4}
def solution(n):
        if n in dpvalue:
            return dpvalue[n]
        else:
            for i in range(4,n+1):
                dpvalue[i] = dpvalue[i-1]+dpvalue[i-2]+dpvalue[i-3]

        return dpvalue[n]
for _ in range(testcase):
    n = int(input())
    if n ==1: print(1)
    elif n==2: print(1)
    elif n==3: print(3)
    else:
        print(solution(n))