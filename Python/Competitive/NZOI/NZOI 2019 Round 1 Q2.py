dic = {"G":0 ,"C":0 ,"E":0 ,"P":0 ,"L":0 ,"S":0}
lst = list(input().split())

while lst[0]!="D":
    dic[lst[0]] += int(lst[1])
    lst = list(input().split())

print(*dic.values())
