vowels = ["a","A","e","E","i","I","o","O","u","U"]
while True:
    string = input()
    if string == "#":
        break
    ans = 0
    for i in vowels:
        ans+=string.count(i)
    print(ans)