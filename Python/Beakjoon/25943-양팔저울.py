n = int(input())
lst = list(map(int,input().split()))
scaleL, scaleR = lst[0], lst[1]
weights = [100,50,20,10,5,2,1]
ans = 0

for i in range(2,n):
    if scaleR == scaleL:
        scaleL += lst[i]
    elif scaleR > scaleL:
        scaleL += lst[i]
    else:
        scaleR += lst[i]

diff = abs(scaleR-scaleL)
for i in weights:
    ans += diff//i
    diff -= (diff//i)*i
print(ans)