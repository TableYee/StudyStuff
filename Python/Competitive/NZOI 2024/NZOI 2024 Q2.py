import sys
input = sys.stdin.readline
n = int(input().rstrip())
mo = [[i,False] for i in range(1,n+1)]
# #assuming median mountains maximise the enjoyment & can be greedy
# cur = n//2
# mo[cur-1][1] = True
# print(cur, end=' ')

# for i in range(n-1):
#     index = max(mo, key=lambda x: -1 if x[1] else abs(x[0]-cur))[0]
#     print(index, end=' ')
#     mo[index-1][1] = True
#     cur = index

from itertools import permutations 
mo = permutations([i for i in range(1,n+1)])
maxDist = [-1,[]]
ans = []
lexi = []
for i in mo:
    tmpDist = 0
    for j in range(1,n):
        tmpDist+=abs(i[j]-i[j-1])
    if tmpDist >= maxDist[0]:
        ans.append([i,tmpDist])
        maxDist = [tmpDist,i]
for i in range(len(ans)):
    if ans[i][1] == ans[-1][1]:
        print(ans[i][0])
        break


# from itertools import permutations 
# import sys
# input = sys.stdin.readline
# n = int(input().rstrip())
# mo = permutations([i for i in range(1,n+1)])
# maxDist = [-1,[]]

# for i in mo:
#     tmpDist = 0
#     for j in range(1,n):
#         tmpDist+=abs(i[j]-i[j-1])
#     if tmpDist > maxDist[0]:
#         maxDist = [tmpDist,i]
#     elif tmpDist == maxDist[0] and sorted([i,maxDist[1]])[0] == i:
#         maxDist = [tmpDist,i]
# print(*maxDist[1])