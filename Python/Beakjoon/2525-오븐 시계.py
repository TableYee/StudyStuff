a,b = map(int,input().split())
c = int(input())
h,m = c//60, c%60
chk = False
b += m
if b>59:
    b = b-60
    h+=1
a+=h
print("%d %d"%(a%24,b))
