x,y,a,b = map(int,input().split())
A = (max(x,y)//min(a,b))*(min(x,y)//max(a,b))
B = (max(x,y)//max(a,b))*(min(x,y)//min(a,b))
print(max(A,B))