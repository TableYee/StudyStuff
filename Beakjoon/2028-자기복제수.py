t = int(input())

for i in range(t):
    n = int(input())
    nsqr = n**2
    if str(nsqr)[-len(str(n)):] == str(n):
        print("YES")
    else: 
        print("NO")