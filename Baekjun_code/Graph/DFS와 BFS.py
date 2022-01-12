from queue import Queue

N, M, start_node = map(int,input().split())
start_node -=1
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    # 편한 인덱싱을 위해 1을 다 빼고 나중에 1을 더한다.
    a -=1
    b -=1
    graph[a].append(b)
    graph[b].append(a)
# 작은 노드를 먼저 돌기위해서 sort
graph =list(map(sorted,graph))

def DFS(graph,start):
    visit = [start]
    stack = [start]
    cur = start
    
    while stack:
        # cur와 연결된 노드를 모두 돌았는지 확인하는 flag
        flag= True
        for node in graph[cur]:
            if node in visit:
                pass
            else:
                visit.append(node)
                stack.append(node)
                cur = node
                flag =False
                break
        if flag:
            stack.pop()
            if stack: cur = stack[-1]
    return [i+1 for i in visit]


def BFS(graph,start):
    visit = [start]
    que = Queue()
    que.put(start)
    while not que.empty():
        cur = que.get()
        if cur not in visit: visit.append(cur)
        else:
            for node in graph[cur]:
                if node not in visit:
                    que.put(node)
                    visit.append(node)
    return [i+1 for i in visit]

print(*DFS(graph,start_node))
print(*BFS(graph,start_node))