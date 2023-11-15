"""
 8 4  6  1  4
1 9 13 19 20 24

C : 5
Min = 1
Ans = 4

C : 4
Min = 4
Ans = 5

C : 3
Min = 3
Ans = 11

C : 2
Min = 11
Ans = 23
"""
import sys
n,c = map(int,sys.stdin.readline().rstrip().split())
lst = [int(sys.stdin.readline().rstrip()) for i in range(n)]
lst.sort()
sub = [lst[i+1] - lst[i] for i in range(n-1)]
dMin, dMax = 1, lst[-1]

while dMax >= dMin:
   cur,cnt = 0,1
   mid = dMin + (dMax-dMin)//2

   for i in range(1,n):
      if lst[i] - lst[cur] >= mid:
         cnt+=1
         cur = i
   if cnt >= c:
      ans = mid
      dMin = mid+1
   else:
      dMax = mid-1
print(ans)

"""
for i in range(n-c):
    m = min(sub) #차의 값들중 최솟값
    idx = sub.index(m) #최솟값의 인덱스
    print(len(sub[idx:]) > len(sub[:idx-1]))
    print(m,idx)
    
    if idx == len(sub)-1: #만약 끝에 있다면
       sub[idx-1] += sub.pop(idx)
    elif idx == 0: #만약 시작에 있다면
       sub[idx] = sub[idx+1] + sub.pop(idx)
    else: #만약 중간에 있다면
         if sub[idx-1] >= sub[idx+1]:
            sub[idx] = sub[idx+1] + m
         if sub[idx-1] <= sub[idx+1]:
            sub[idx-1] += m
         else: #최솟값이 어느쪽끝에 있는가?
            if len(sub[idx:]) > len(sub[:idx-1]):
               sub[idx-1] += sub.pop(idx)
            else:
               sub[idx] = sub[idx+1] + sub.pop(idx)
print(min(sub))
"""