t = int(input())

for i in range(t):
    ans = 0
    s = input()
    for j in range(65,91):
        if not chr(j) in s:
            ans+=j
    print(ans)
        