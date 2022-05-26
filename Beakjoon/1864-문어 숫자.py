import math
notes = ["-","\\","(","@","?",">","&","%","/"]
while True:
    code = [i for i in input()]
    code = code[::-1]
    ans = 0

    if code[0] == "#":
        break

    for i in range(len(code)):
        idx = notes.index(code[i])
        if idx == 8: idx = -1

        ans += int(idx*math.pow(8,i))
    print(ans)