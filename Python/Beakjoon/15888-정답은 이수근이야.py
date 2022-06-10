a, b, c = map(int,input().split())
pows = [2, 4, 8, 16, 32, 64]
root = 0
proot = 0
for x in range(-100, 101):
    if a*x*x + b*x + c == 0:
        root+= 1
        if x in pows: proot+= 1
if root != 2: print("둘다틀렸근")
else: print("이수근" if proot == 2 else "정수근")