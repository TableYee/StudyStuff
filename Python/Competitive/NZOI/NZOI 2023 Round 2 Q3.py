# n = int(input())
# stitches = [0] * 6
# cur = 0

# for i in range(n):
#     ins = input()
#     x = int(ins[1:])
#     lenStitches = len(stitches)

#     if ins[0] == 'I':
#         stitches[cur:cur+1] = [stitches[cur]+1]*x
#         cur = cur+x if cur+x < len(stitches) else 0
#     else:
#         if cur+x < lenStitches:
#             maxStitches = max(stitches[cur:cur+x])
#             del stitches[cur:cur+x]
#             stitches.insert(cur, maxStitches+1)
#             cur+=1
#         else:
#             maxStitches = max(stitches[cur:cur+x]+stitches[:cur+x-lenStitches])
#             del stitches[cur:cur+x]
#             del stitches[:cur+x-lenStitches]
#             cur = 0
#             stitches.insert(cur, maxStitches+1)
# cur = 0 if cur == 0 and ins[0] == "D" else cur-1
# print(len(stitches),stitches[cur],sep='\n')
n = int(input())
stitches = [0] * 6
cur = 0

for i in range(n):
    ins = input()
    x = int(ins[1:])
    lenStitches = len(stitches)

    if ins[0] == 'I':
        x = int(ins[1:])
        for _ in range(x):
            stitches[cur] += 1
            cur = (cur + 1) % 6
    
    elif ins[0] == 'D':
        x = int(ins[1:])
        max_stitches = max(stitches[cur:cur + x] + stitches[:x - (6 - cur)])
        for i in range(x):
            if i < 6 - cur:
                stitches[i] = stitches[cur + i]
            else:
                stitches[i] = 0
        stitches[0] = max_stitches + 1
        cur = 0

unused_stitches = sum(stitches)
last_row = max(stitches)

print(unused_stitches)
print(last_row)

