import heapq as hq
def solution(operations):
    answer =[]
    que = []
    for oper in operations:
        command = oper.split()[0]
        num = int(oper.split()[1])
        if command =="I":
            hq.heappush(que,num)
        elif command =="D" and num==-1 and que:
            hq.heappop(que)
        elif command =="D" and num==1 and que:
            maxnum = hq.nlargest(1,que)[0]
            que.remove(maxnum)

    if not que:
        return [0,0]
    else:
        answer.append(hq.nlargest(1,que)[0])
        answer.append(que[0])
        return answer


a = ["I 16","D 1"]
print(solution(a))
b = ["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"]
print(solution(b))

# 이번문제에서는 이중 우선순위 큐를 구현했다. 다른 사람은 min max heap을 두개 만들었지만
# 나는 heapq의 메소드인 nlargest를 이용해서 heap의 최대값을 구하는 방식으로 최대힙을 구현하지 않았다.
# 맨날 heapq를 쓸때마다 헷갈리는데 heapq는 return 하지 않고 그대로 변수로 들어오느iter를 replace한다.
# 즉 list를 heapq로만 연산해가면 list는 자동으로 우선순위 큐를 유지한다.