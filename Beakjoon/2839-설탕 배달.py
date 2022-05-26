n = int(input())
ans = []

for i in range(n//5+1):
    n2 = n - (5*i)
    if n2 % 3 == 0:
        ans.append((n2//3) + i)
if ans: print(min(ans))
else: print(-1)