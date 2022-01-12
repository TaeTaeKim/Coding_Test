import sys
sys.setrecursionlimit(10**6)
dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]
def DFS(i,j,Map,visit,width,height):
    for index in range(8):
        nx = i + dx[index]
        ny = j + dy[index]
        if nx<0 or nx>=height or ny<0 or ny>=width:
            continue
        elif Map[nx][ny] ==0 or visit[nx][ny]:
            continue
        else:
            visit[nx][ny] = True
            DFS(nx,ny,Map,visit,width,height)
    return
    

def solution():
    while True:
        iscnt = 0
        width,height = input().split()
        if width=='0' and height=='0':
            break
        width = int(width)
        height = int(height)
        visit = [[False for _ in range(width)] for _ in range(height)]
        Map = []
        for _ in range(height):
            line = input().split()
            tolistline = [int(x) for x in line]
            Map.append(tolistline)


        for i in range(height):
            for j in range(width):
                if Map[i][j] ==0 or visit[i][j]:
                    continue
                else:
                    iscnt +=1
                    visit[i][j] = True
                    DFS(i,j,Map,visit,width,height)
        
        print(iscnt)
    return

solution()