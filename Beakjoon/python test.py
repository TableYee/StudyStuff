def check():
    global large
    for j in range(N):
        check = [arr[i][j] for i in range(N)]
        for _ in ["C", "P", "Z", "Y"]:
            large = max(large,arr[j].count(_))
            large = max(large,check.count(_))
    return 0
N = int(input())
arr = []
for i in range(N):
    arr.append(list(input()))
large = 0
check()

for x in range(N):
    for y in range(N):
        if y+1 < N:
            arr[x][y],arr[x][y+1] = arr[x][y+1],arr[x][y]
            for i in range(N):
                print(*arr[i])
            print()
            check()
            arr[x][y],arr[x][y+1] = arr[x][y+1],arr[x][y]
            
        if x+1 < N:
            arr[x][y],arr[x+1][y] = arr[x+1][y],arr[x][y]
            for i in range(N):
                print(*arr[i])
            print()
            check()
            arr[x][y],arr[x+1][y] = arr[x+1][y],arr[x][y]
            
print(large)

