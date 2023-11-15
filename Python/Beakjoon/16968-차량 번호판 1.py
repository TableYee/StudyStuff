s = input()
ans,end,sub = 1,0,0

for i in range(len(s)):
    sub=0
    if len(s)==i+1: #if reaches end
        for j in range(end,i+1):
            ans*=26-sub if s[i] == "c" else 10-sub
            sub+=1
        break
    if s[i]!=s[i+1]: #if the letter changes
        for j in range(end,i+1):
            ans*=26-sub if s[i] == "c" else 10-sub
            sub+=1
        end = i+1
print(ans)

"""
def calc(stack,r):
    length = len(stack)-1
    if length in [1,2]:
        if stack[-1] == "d":
            return r * 10
        else:
            return r * 26
    else:
        if stack[-1] == "d":
            return r * 10**length*length
        else:
            return r * 26**length*length

n = input()
ans = 10**n.count("d") * 26**n.count("c")
stack = [0]
r,high = 1,0
#print(ans)
for i in range(len(n)):
    if n[i] == stack[-1] or stack[-1] == 0:
        stack.append(n[i])
        continue
    else:
        #print(stack,r)
        r = calc(stack,r)
        high = max(len(stack),high)
        stack = [0,n[i]]
r = calc(stack,r)
high = max(len(stack),high)

if high > 2:
    print(ans-r)
else:
    print(ans)
"""