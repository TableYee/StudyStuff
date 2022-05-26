def divAlgo(a,b):
    remain1 = a%b
    remain2 = b
    #print("-----------")
    #print(remain1,remain2)
    while remain1 > 0:
        remain1,remain2 = max(remain1,remain2) % min(remain1,remain2),remain1
        #print(remain1,remain2)
    return remain2

for _ in range(int(input())):
    lst = list(map(int,input().split()))
    ans = 0

    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if i == j: continue
            ans = max(ans,divAlgo(lst[i],lst[j]))
    print(ans)