import sys
map = []
size = int(input())
for _ in range(size):
    line = input()
    tolistline = [int(x) for x in line]
    map.append(tolistline)
visit = []
for _ in range(size):
    visit.append([False for i in range(size)])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def DFS(i,j,map,visit):
    room = 0
    for index in range(4):
        nx = i+dx[index]
        ny = j+dy[index]
        if nx<0 or nx>=size or ny<0 or ny>=size:
            continue
        elif map[nx][ny] ==0 or visit[nx][ny]==True:
            continue
        else:
            visit[nx][ny] = True
            room +=1
            room +=DFS(nx,ny,map,visit)
    return room

def solution():
    apart = 0
    room = []    
    for i in range(size):
        for j in range(size):
            if map[i][j]==0:
                continue
            # map이 1일때 즉 사람이 사는곳 일때
            elif map[i][j]==1 and (not visit[i][j]):
                visit[i][j] = True
                apart +=1
                # 1이면 bfs돈다.
                room.append(DFS(i,j,map,visit))
    print(apart)
    room = sorted(room)
    return [x+1 for x in room]

print(*solution())