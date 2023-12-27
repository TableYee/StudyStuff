s = input()
prev = ''
ans = 1

for i in s:
    multiplier = 10 if i == 'd' else 26
    if i == prev:
        ans *= multiplier-1
    else:
        ans *= multiplier
    prev = i
print(ans)