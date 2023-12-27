T = int(input())
for i in range(T):
    votes = int(input())
    print("++++ " * (votes//5) + "|" * (votes%5))