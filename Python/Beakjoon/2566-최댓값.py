maxNum = 0
ans = [1,1]
for i in range(9):
    lst = list(map(int,input().split()))
    for j in range(9):
        if lst[j] > maxNum:
            maxNum = lst[j]
            ans = [i+1,j+1]
print(maxNum)
print(*ans)