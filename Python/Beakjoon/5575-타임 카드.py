for i in range(3):
    h,m,s,fh,fm,fs = map(int,input().split())
    if fs < s:
        fs = fs+(60-s)
        fm-=1
    else:
        fs = fs-s
    if fm < m:
        fm = fm+(60-m)
        fh-=1
    else:
        fm = fm-m
    fh = fh-h
    print(fh,fm,fs,sep=' ')