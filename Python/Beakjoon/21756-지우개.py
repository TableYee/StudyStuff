n = int(input())
lst = [i for i in range(1,n+1)]

while len(lst) != 1:
    lst = [lst[i] for i in range(1,len(lst),2)]
print(lst[0])