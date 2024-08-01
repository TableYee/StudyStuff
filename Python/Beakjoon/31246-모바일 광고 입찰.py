n,k = map(int,input().split())
bid = 0
dif = [0]

for i in range(n):
    a,b = map(int,input().split())
    if a-b >= 0:
        bid+=1
    else:
        dif.append(b-a)
dif.sort()

print(dif[k-bid if bid<k else 0])