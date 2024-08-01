def Distance(vals):
    vals.sort()
    dist = 0
    median = vals[len(vals)//2]
    for i in vals:
        dist += abs(i - median)
    return dist

n = int(input())
cols,rows = [],[]

for i in range(n):
    col, row = map(int,input().split())
    cols.append(col)
    rows.append(row)

print(min(Distance(cols), Distance(rows)))