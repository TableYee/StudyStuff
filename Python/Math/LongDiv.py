def longDiv(a, b):
    ans = 0
    count = 1
    calc_b = b
    string = ["%d/%d" % (a, calc_b)]

    #while calc_b > 0:
    for i in range(8):
        rounds = 0
        count *= 10
 
        if a > calc_b:
            a /= count
            continue

        while a*rounds < calc_b:
            rounds += 1

        if a*rounds > calc_b:
            rounds -= 1

        ans += rounds/(count/10)
        print(a)
        print(" "*(len(str(a))+len(str(calc_b))) + str(ans))
        calc_b = float(Decimal(b)-Decimal((a*rounds)))
        string.append("\n" + " "*(max([len(string[i]) for i in range(len(string))])-1) + "%s" % (Decimal(str(a*rounds))))
        string.append("\n" + " "*(max([len(string[i]) for i in range(len(string))])//2) +"-"*max(len(str(a*rounds))+1, len(str(calc_b))+1))
        string.append("\n" + " "*(max([len(string[i]) for i in range(len(string))])-1) + "%s" % (Decimal(str(calc_b))))
        
        for i in string:
            print(i,end=' ')
        print()

from decimal import Decimal, getcontext
getcontext().prec = 3

x, y = map(int, input().split())
longDiv(x, y)
