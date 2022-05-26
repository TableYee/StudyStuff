def calc(lst):
    n = 1
    for i in lst:
        n = n*(i+1)
    return n-1

for i in range(int(input())):
    n = int(input())
    clothes = {}
    for i in range(n):
        name, type = map(str,input().split())
        if type in clothes.keys():
            clothes[type] += 1
        else:
            clothes[type] = 1
    if len(clothes) < 2:
        print(n)
    else:
        print(calc(list(clothes.values())))
#ac,ad,ae,af,bc,bd,be,bf,ca,cb,ce,cf,da,db,de,df,ea,eb,ec,ed,fa,fb,fc,fd 6*4/2 =12
#ace,acf,ade,adf,bce,bcf,bde,bdf,c~~ = 6*2*2/3!
#ace aec cae cea eac eca 6