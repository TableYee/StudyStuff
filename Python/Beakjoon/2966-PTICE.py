n = int(input())
m = [i for i in input()]
adrian,bruno,goran = ["A","B","C"], ["B","A","B","C"], ["C"*2,"A"*2,"B"*2]
dic = {"adrian":0,"bruno":0,"goran":0}

for i in range(n):
    if adrian[i%len(adrian)] == m[i]:
        dic["adrian"] += 1
    if bruno[i%len(adrian)] == m[i]:
        dic["bruno"] += 1
    if goran[i%len(adrian)] == m[i]:
        dic["goran"] += 1
print(max(dic.values()))
print(dic.get(1))