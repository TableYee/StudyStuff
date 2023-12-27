n,m = map(int,input().split())
r,c,d = map(int,input().split())
floor = [[*map(int,input().split())] for i in range(n)]
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1] 
cnt, fin = 0, False

while not fin:
    if floor[r][c] == 0:
        floor[r][c] = 2
        cnt+=1

    for i in range(4):
        d = (d+3) % 4
        nr,nc = r+dr[d], c+dc[d]

        if floor[nr][nc] == 0:
            r,c = nr,nc
            break

    if floor[r][c] != 0:
        nr,nc = r-dr[d], c-dc[d]
        if floor[nr][nc] == 1:
            print(cnt)
            break
        r,c = r-dr[d],c-dc[d]