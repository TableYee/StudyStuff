balls = [1,0,0]
for i in range(int(input())):
    a,b = map(int,input().split())
    a-=1
    b-=1
    balls[a],balls[b] = balls[b],balls[a]
print(balls.index(1)+1)