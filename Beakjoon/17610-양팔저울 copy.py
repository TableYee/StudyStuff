import time
k = int(input())
lst = list(map(int,input().split()))
lst.sort()
s = sum(lst)

#13
#1 3 9 27 81 243 729 2187 6561 19683 59049 177147 200000

ans = [lst[0]]
for i in range(1,k):
    temp = [lst[i]]

    for j in ans:
        temp += [j + lst[i], abs(j-lst[i])]
    ans += temp
ans = list(set(ans))
if 0 in ans: ans.remove(0)
print(s - len(ans))
"""
import time
k = int(input())
lst = dict([i,[i]] for i in list(map(int,input().split())))
s = sum(lst)
cnt = []
asd = 0
#13
#1 3 9 27 81 243 729 2187 6561 19683 59049 177147 200000

for i in range(k):
    a,b = list(lst.keys()),list(lst.items())
    for j in range(i+1,len(lst)):
        if a[i] in b[j][1]: 
            continue
        if not a[i] + a[j] in lst:
            lst[a[i] + a[j]] = [a[i],*b[j][1]]
        if not abs(a[i] - a[j]) in lst:
            lst[abs(a[i] - a[j])] = [a[i],*b[j][1]]
print(s - len(lst.keys()))
"""