import itertools
import math
################# 정답
#행별로 보면 i번째 도시에서 j번째도시로 가는 비용이다.
def solution():
    from_to = []
    N = int(input())
    # 데이터 입력
    for _ in range(N):
        row = list(map(int,input().split(" ")))
        from_to.append(row)

    routes = list(itertools.permutations(range(N)))
    cost = math.inf
    for route in routes:
        cost_temp = 0 
        flag = False
        if  from_to[route[-1]][route[0]]==0:
            flag = True
            break          
        for i in range(len(route)-1):
            if from_to[route[i]][route[i+1]]==0:
                flag = True
                break
            else:
                cost_temp += from_to[route[i]][route[i+1]]
                # 이 부분이 생명
                if cost_temp>cost:
                    flag = True
                    break
        if flag:
            continue
        cost_temp +=from_to[route[-1]][route[0]]
        cost = min(cost,cost_temp)
    print(cost)
solution()



################# 첫 번쨰 시도
#행별로 보면 i번째 도시에서 j번째도시로 가는 비용이다.
from_to = []
N = int(input())
# 데이터 입력
for _ in range(N):
    row = list(map(int,input().split(" ")))
    from_to.append(row)

# 한 루트의 Cost
def routeCost(route):
    cost = 0
    for j in range(len(route)-1):
        if from_to[route[j]][route[j+1]] ==0:
            return math.inf
        else:
            cost += from_to[route[j]][route[j+1]]
    cost +=from_to[i][route[0]]
    cost +=from_to[route[N-2]][i]
    return cost


start ={}
# 시작점별 회귀하는 비용을 구하기 위해 도시개수 만큼 반복
for i in range(N):
    cities = [k for k in range(N)]
    cities.pop(i)
    # 시작점을 제외한 다른 도시들을 갈 수 있는 모든 경우를 저장.
    routes = list(itertools.permutations(cities,len(cities)))
    # 모든 경우의 Cost를 담을 수 있는 value변수
    value = []
    for route in routes:
        # start가 시작할 수 없거나 회귀못하는 도시는 제외
        if from_to[i][route[0]] ==0:
            value.append(math.inf)
        elif from_to[route[N-2]][i] ==0:
            value.append(math.inf)
        else:
            value.append(routeCost(route))
    start[i] = min(value)

print(min(start.values()))