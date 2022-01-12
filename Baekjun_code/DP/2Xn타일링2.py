dpvalue = {1:1,2:3}
n = int(input())

def solution(n):
    if n in dpvalue:
        return dpvalue[n]
    else:
        for i in range(3,n+1):
            dpvalue[i] = solution(i-1)+ (2*solution(i-2))
    
    return dpvalue[n]


print(solution(n))

