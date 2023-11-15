def Bin(num):
    cMin, cMax = 0,n-1
    while cMax >= cMin:
        cMid = (cMax+cMin)//2
        #print(cMin, cMid, cMax, num ,A[cMid])
        if A[cMid] == num:
            return 1
        elif A[cMid] > num:
            cMax = cMid-1
        else:
            cMin = cMid+1
    return 0

n = int(input())
A = list(map(int,input().split()))
A.sort()
m = int(input())
B = list(map(int,input().split()))


for i in B:
    print(Bin(i))