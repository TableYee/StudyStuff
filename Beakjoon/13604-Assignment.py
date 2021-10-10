n = int(input())
point = []
ans = 0
for i in range(n):
    point.append(list(map(int,input().split())))
point.sort(reverse=True)

for i in range(point[0][0],0,-1):
    chk = []
    for j in range(len(point)):
        if point[j][0] >= i:
            chk.append([point[j][1],j])
        else:
            break
    #print(chk)
    if chk:
        ans += max(chk)[0]
        del point[max(chk)[1]]
print(ans)