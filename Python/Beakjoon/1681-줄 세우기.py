n,l = map(int,input().split())
ans,i = 0,0

while i < n:
    ans += 1
    if not str(l) in str(ans):
        i+=1

print(ans)