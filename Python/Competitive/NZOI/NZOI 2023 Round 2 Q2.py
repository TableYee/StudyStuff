from math import ceil
n = int(input())
lst = list(map(int,input().split()))

print((ceil(sum(lst)/n)*n)-sum(lst))