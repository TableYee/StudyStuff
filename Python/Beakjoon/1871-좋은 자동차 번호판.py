def asd(num):
    cnt = len(num)-1
    ret = 0
    for i in num:
            ret += (ord(i)-65)*26**cnt
            cnt-=1
    return ret

for i in range(int(input())):
    string,integer = map(str,input().split('-'))
    if abs(asd(string)-int(integer)) <= 100:
        print("nice")
    else:
        print("not nice")
