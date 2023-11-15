def strikeChk(inpN, chkN, cntS):
    tmp = 0

    for i in range(3):
        if inpN[i] in chkN:
            if chkN.index(inpN[i]) == i:
                tmp+=1
    if tmp == cntS: return True
    else: return False

def ballChk(inpN,chkN,cntB):
    tmp = 0

    for i in range(3):
        if inpN[i] in chkN:
            if chkN.index(inpN[i]) != i:
                tmp+=1
    if tmp == cntB: return True
    else: return False

n = int(input())
lst = [list(map(int,input().split())) for i in range(n)]
ans = 0

for i in range(1,10):
    for j in range(1,10):
        if i == j:
            continue
        for l in range(1,10):
            if j == l or l == i:
                continue
            tmpAns = 0
            curN = str(i)+str(j)+str(l)

            for chk in lst:
                chkN = str(chk[0])
                
                if strikeChk(curN, chkN, chk[1]) and ballChk(curN, chkN, chk[2]):
                    tmpAns+=1
                else: break
            if tmpAns == n:
                ans+=1      

print(ans)