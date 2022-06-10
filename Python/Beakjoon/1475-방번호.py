a,b = map(int,input().split())
y,x = 0,b-1
bol,skip = False,False

lst = [j for j in range(1,a*b+1,1)]
ans = [[' ' for i in range(b)] for j in range(a)]

for i in range(a*b):
     ans[y][x] = lst[i]

     if y <= 0 and bol or y >= a-1 and not bol:
          bol = False if bol else True
          x-=1
          skip = True
     if skip:
          skip = False
          continue
     
     if bol: y-=1
     else: y+=1

for i in ans:
     print(*i)