trash = input()
helmet = list(map(int,input().split()))
vest = list(map(int,input().split()))
print(max(helmet) + max(vest))