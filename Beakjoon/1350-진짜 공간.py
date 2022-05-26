import math
n = int(input())
files = list(map(int,input().split()))
cluster = int(input())
total = 0

for i in files:
    total+=cluster*math.ceil(i/cluster)
print(total)