n = int(input())
alpha = [0]*26
ans = ""

for i in range(n):
    alpha[ord(input()[0])-97] += 1

for i in range(26):
    if alpha[i] >= 5:
        ans+=chr(i+97)
if ans:print(ans)
else:print("PREDAJA")