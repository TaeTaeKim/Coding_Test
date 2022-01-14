import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    cnt = 0
    while scoville[0]<K:
        if len(scoville)<=1:
            return -1
        new = hq.heappop(scoville) + hq.heappop(scoville)*2
        hq.heappush(scoville,new)
        cnt +=1
    return cnt

scoville = [1, 2]
print(solution(scoville,7))