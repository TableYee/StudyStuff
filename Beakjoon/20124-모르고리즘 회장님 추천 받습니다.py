n = int(input())
maxName, maxPoint = "",0

for i in range(n):
    name,point = map(str,input().split())
    point = int(point)
    if point > maxPoint:
        maxName = name
        maxPoint = point
    elif point == maxPoint:
        maxName = sorted([name,maxName])[0]
print(maxName)
