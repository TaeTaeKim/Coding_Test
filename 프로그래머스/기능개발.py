import math
from collections import deque
def solution(progress,speeds):
    answer = []

    # 완료까지 필요한 날짜를 반환하는 기능
    date =deque([math.ceil(x/y) for x,y in zip([100-x for x in progress],speeds)])
    print(date)
    prev = date.popleft()
    cnt = 1
    while date:
        k = date.popleft()
        if k<=prev:
            cnt +=1
            continue
        else:
            answer.append(cnt)
            cnt=1
            prev =k
    answer.append(cnt)
    return answer


# 앞에서 먼저 꺼내야하는 문제로 큐를 이용하면 빠른 연산을 할 것으로 예상하여 deque를 사용
# list comprehension함수를 적극 이용하여 적은 코드 메모리 절약
# 마지막에 prev 재할당 과정에서 k = prev로 잘 못 할당하여 오류가 났었음