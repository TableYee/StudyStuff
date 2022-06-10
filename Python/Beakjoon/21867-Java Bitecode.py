a = input()
lst = input()
ans = []

for i in lst:
    if i != 'J' and i != 'A' and i != 'V':
        ans.append(i)
        
if not ans:
    print("nojava")
else:
    print(*ans,sep='')