normal = input()
key = input()
ans = ''

for i in range(len(normal)):
    sub = 96 + ord(normal[i]) - ord(key[i%len(key)])

    if normal[i] == ' ':
        ans += ' '
    elif sub < 97:
        ans += chr(122 - (96 - sub))
    else:
        ans += chr(sub)
print(ans)

