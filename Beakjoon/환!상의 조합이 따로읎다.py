c = list(map(int,input().split()))
ans=0
d = list(map(int,input().split()))

def stuff(a,b):
     global c,d,ans
     if a == c[1]-1:
          ans+=(b==c)
          return ans
     stuff(a+1, b)
     stuff(a+1, b+d[a])

print(stuff(0,c[0]))
