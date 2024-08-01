from collections import deque

def tilt(dir,ball,mp):
    bx,by = map(int, ball)
    move = 0
    while mp[by+dir[1]][bx+dir[0]] != "#" and mp[by][bx] != "O":
        move+=1
        bx += dir[0]
        by += dir[1]
    return [bx,by,move]

n,m = map(int,input().split())
mp = [input() for i in range(n)]
dir = [[0,1],[0,-1],[1,0],[-1,0]]
que = deque()
cnt = [1]
visited = []

for i in range(n):
    for j in range(m):
        if mp[i][j] == "R":
            rCord = [j,i]
        if mp[i][j] == "B":
            bCord = [j,i]

while True:
    for j in range(4):
        nrx,nry,rcnt = map(int, tilt(dir[j], rCord, mp)) # red
        nbx,nby,bcnt = map(int, tilt(dir[j], bCord, mp)) # blue

        if mp[nby][nbx] == "O":
            continue
        if mp[nry][nrx] == "O":
            print(cnt[0])
            quit()

        if [nrx,nry] == [nbx,nby]:
            if rcnt > bcnt:
                nrx-=dir[j][0]
                nry-=dir[j][1]
            else:
                nbx-=dir[j][0]
                nby-=dir[j][1]  
        if (nrx, nry, nbx, nby) not in visited:
            visited.append((nrx, nry, nbx, nby))      
            que.append([[nrx,nry],[nbx,nby],[cnt[0]+1]])
    if not que:
        print(-1)
        break
    rCord, bCord, cnt = map(list, que.popleft())
    if cnt[0] > 10:
        print(-1)
        break
