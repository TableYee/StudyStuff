import math
a,b = map(int,input().split())
x1,y1 = math.ceil(a/4),(a-1)%4+1
x2,y2 = math.ceil(b/4),(b-1)%4+1
print((max(x1,x2)-min(x1,x2))+(max(y1,y2)-min(y1,y2)))