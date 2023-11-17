def strChk(str):
    cnt = 0
    for i in ['a','e','i','o','u']:
        cnt += str.count(i)
    if cnt >= 1 and len(str)-cnt >= 2: 
        return True
    else: 
        return False

def pwdMaker(cur, pwd, chrlst):
    if cur >= l:
        if strChk(pwd):
            print(pwd)
        return 
    if pwd == "":
        for i in chrlst:
            pwdMaker(cur+1, pwd+i, chrlst)
    else:
        for i in chrlst[chrlst.index(pwd[-1])+1:]:
            pwdMaker(cur+1, pwd+i, chrlst)
    

l,c = map(int,input().split())
chars = list(map(str, input().split()))
chars.sort()


pwdMaker(0,"",chars)