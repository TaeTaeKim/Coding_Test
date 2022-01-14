# 내가 푼 풀이 : 큐와 튜플을 이용한 검출법

# 초반에 인쇄순서를 반환하는 알고리즘은 완성했지만
# location을 detect할 방법을 찾다가 tuple로 각자의 index를 같이 보내도록함
from collections import deque
def solution(priorities,location):
    maxprior = max(priorities)
    cnt = 0
    # 10을 타겟으로 설정
    prior = deque([(g,i) for i,g in enumerate(priorities)])
    print(prior)
    while prior:
        docu = prior.popleft()
        if docu[0]<maxprior:
            prior.append(docu)
        else:
            cnt +=1
            if docu[1]==location:
                return cnt
            # max 나 min 모두 iterable에 key를 줘서 구하면 iter그자체 자료형으로 반환하므로
            # [0]을 해줘야 int를 받는다.
            if prior:
                maxprior = max(prior,key=lambda x:x[0])[0]

# 다른 사람의 풀이 분석: any를 사용한 조금더 효율적인 반복문 max를 쓰지 않아서 시간효율
def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

priorities =[1, 1, 9, 1, 1, 1]	
print(solution2(priorities,0))