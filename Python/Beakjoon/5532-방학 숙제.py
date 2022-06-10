l = int(input())
a,b,c,d = map(int,[input() for i in range(4)])
a = a/c 
b = b/d
print(int(l - max(a,b)))