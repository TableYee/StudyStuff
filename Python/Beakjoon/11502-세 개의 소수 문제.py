#2 3 5 7 11 13
#2 + 3 = 5
#4 + 3 = 7
#4 + 5 = 9
#4 + 7 = 11
#2 + 11 = 13 3 + 3 + 7 = 13
#4 + 11 = 15
#4 + 13 = 17
#2 + 17 = 19 3 + 3 + 13 = 19 5 + 7 + 7 = 19
#2 + 19 = 21
#4 + 19 = 23
#2 + 23 = 25 3 + 3 + 19 = 25 5 + 7 + 13 = 25
def primeNumber(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i): 
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

t = int(input())
prime = primeNumber(1000)

def search(n):
    global prime
    lst = prime
    if n in lst:
        return lst[lst.index(n)-1]
    while len(lst) != 1:
        if lst[len(lst)//2] < n:
            lst = lst[len(lst)//2:]
        else:
            lst = lst[:len(lst)//2]
    return lst[0]

for i in range(t):
    k = int(input())
    fprime = search(k)
    while True:
        if (k-fprime)%2 == 0 and (k-fprime)//2 in prime:
            lst = [(k-fprime)//2, (k-fprime)//2, fprime]
            print(*sorted(lst))
            break
        else:
            fprime = search(fprime)
