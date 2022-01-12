# 두 원의 교점 문제이다.
import math
n = int(input())
for _ in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    # 두 원의 위치 관계
    dis = math.sqrt((x1-x2)**2+(y1-y2)**2)
    if dis> abs(r1-r2) and dis<r1+r2:
        print(2)
    elif abs(r1-r2)==dis or r1+r2 ==dis:
        print(1)
    elif dis == r1 and dis == r2:
        print(-1)
    else:
        print(0)