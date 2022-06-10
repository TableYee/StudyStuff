t = int(input())

for i in range(t):
    c = int(input())
    q = c//25
    c -= 25*q
    d = c//10
    c -= 10*d
    n = c//5
    c -= 5*n
    p = c//1
    c -= 1*p
    print(q,d,n,p)