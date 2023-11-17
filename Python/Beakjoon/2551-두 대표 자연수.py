n = int(input())
nums = list(map(int,input().split()))
lst = [0 for i in range(10001)]
minSum = 10**64
ans1, ans2 = 0,0

for i in nums:
    lst[i]+=1

for i in range(1,10000):
    sum1 = 0
    for j in range(1,10000):
        sum1 += abs(i-j)*lst[j]
    if sum1 < minSum:
        minSum = sum1
        ans1 = i

minSum = 10**64
for i in range(1,10000):
    sum2 = 0
    for j in range(1,10000):
        sum2 += (i-j)**2*lst[j]
    if sum2 < minSum:
        minSum = sum2
        ans2 = i
print(ans1,ans2)