n = int(input())
ans = 0

for i in range(n):
    word = input()
    stack, finished = [word[0]], set([])
    
    for j in word[1:]:
        if stack[-1] != j: #마지막이 현재 단어와 겹치지 않을
            if j in finished:
                ans-=1
                break
            finished.add(j)
            finished.add(stack[-1])
            stack.append(j)
    ans+=1
print(ans)
