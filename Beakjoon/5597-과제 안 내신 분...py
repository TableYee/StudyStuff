import sys
message = [i for i in range(1,31)]
for i in range(28):
    message.remove(int(sys.stdin.readline().strip()))
print(message[0])
print(message[1])
