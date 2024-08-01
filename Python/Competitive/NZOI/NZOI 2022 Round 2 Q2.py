n = int(input())
lst = list(map(int,input().split()))
lst.sort()
strength = []

for i in range(n):
    strength.append(lst[i]+lst[n-i-1])

print(max(strength)-min(strength))