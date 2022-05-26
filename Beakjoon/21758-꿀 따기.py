import sys
n = int(sys.stdin.readline().lstrip())
lst = list(map(int,sys.stdin.readline().lstrip().split()))

lst1 = lst[1:n-1]
middle = lst1.index(max(lst1))
bhb = sum(lst1[:middle+1]) + sum(lst1[middle:])

bbh = []
for i in range(1,len(lst)-1):
    lst1 = lst.copy()
    lst1.pop(i)
    bbh.append(sum(lst1[1:]) + sum(lst[i+1:]))
bbh = max(bbh)

lst = lst[::-1]
hbb = []
for i in range(1,len(lst)-1):
    lst1 = lst.copy()
    lst1.pop(i)
    hbb.append(sum(lst1[1:]) + sum(lst[i+1:]))
hbb = max(hbb)

print(max(bhb,bbh,hbb))