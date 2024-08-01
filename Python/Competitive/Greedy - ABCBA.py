from collections import deque

s = [i for i in input()]
lst = deque()
ans = 0
i = 0

for i in range(len(s)):
    if s[i] == "B":
        lst.append(i)
    elif s[i] == "C" and len(lst) > 0:
        s[i] = ''
        s[lst.popleft()] = ''
        ans+=1

lst = deque()
for i in range(len(s)):
    if s[i] == "A":
        lst.append(i)
    elif s[i] == "B" and len(lst) > 0:
        s[i] = ''
        s[lst.popleft()] = ''
        ans+=1
    i+=1

print(ans)