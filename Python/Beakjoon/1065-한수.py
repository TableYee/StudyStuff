def oneNumber(n):
    lst = list(map(int,str(n)))
    dif = lst[0] - lst[1]
    chk = 0

    for i in range(len(lst)-1):
        if lst[i] - lst[i+1] == dif:
            chk += 1
    if chk == len(lst)-1:
        return 1
    else:
        return 0

n = int(input())
ans = 99
if n < 100:
    print(n)
    quit()
for i in range(100,n+1):
    if oneNumber(i):
        ans+=1
print(ans)