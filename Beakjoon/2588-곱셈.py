num = [int(input()), input()]
add = []

for i in range(2,-1,-1):
    add.append(int(num[1][i])*num[0])
print(*add,sep='\n')
print(add[0] + add[1]*10 + add[2]*100)