import sys
input = sys.stdin.readline
n,m,verA,verB = map(int,input().split())
libA = list(map(str,input().split()))
libVerA = []
for i in range(verA):
    libVerA.append(list(map(int,input().split())))
libB = list(map(str,input().split()))
libVerB = []
for i in range(verB):
    libVerB.append(list(map(int,input().split())))

chkLibs = []
for i in range(n):
    if libA[i] in libB:
        chkLibs.append([i,libB.index(libA[i])])

if not chkLibs:
    print(f'{verA-1} {verB-1}')
    quit()

for i in range(verA-1,-1,-1):
    for j in range(verB-1,-1,-1):
        ans = True
        for A,B in chkLibs:
            if libVerA[i][A] != libVerB[j][B]:
                ans = False
                break
        if ans:
            print(i,j)
            quit()