from queue import Queue
import sys
# 넓이 우선탐색

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
    return visit
def minuslist(node1,node2):
    res =[]
    for i in node2:
        node1.remove(i)
    return node1
    
def solution():
    # 그래프 2차원 array생성.
    N, rel = map(int,sys.stdin.readline().split())
    graph= [[] for _ in range(N)]
    for _ in range(rel):
        a,b = map(int,input().split())
        a-=1
        b-=1
        graph[a].append(b)
        graph[b].append(a)
    node = list(range(N))
    # 첫번째 노드를 BFS한 결과
    
    res = 0
    i=0
    while node:
        res +=1
        BFSres = BFS(graph,node[i])
        node = minuslist(node,BFSres)
        
    return res

print(solution())