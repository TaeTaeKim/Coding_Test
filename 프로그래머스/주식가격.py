from collections import deque
def solution(prices):
    stock = deque(prices)
    answer = [0]*len(prices)
    for k in range(len(prices)):
        price = stock.popleft()
        sub_price = [a-b for a,b in zip(stock,[price]*len(stock))]
        if sub_price ==[]:
            continue
        elif sub_price[0]<0:
            answer[k]+=1
            continue
        else:
            answer[k] +=1
            for i in range(1,len(sub_price)):
                if sub_price[i]>=0:
                    answer[k] +=1
                else:
                    continue
                
    return answer
## 시간초과가 많이뜬다.



# 일단 알고리즘의 기본은 완전탐색으로 해본다.
# 원래는 대소비교부분을 list 인덱싱으로 할것을 deque를 이용한 시간절약
def solution2(prices):
    answer =[0]* len(prices)
    prices = deque(prices)
    for i in range(len(prices)):
        price = prices.popleft()
        for j in prices:
            if price<=j:
                answer[i] +=1
            else:
                answer[i] +=1
                break
    return answer


print(solution2([1,2,3,2,3]))