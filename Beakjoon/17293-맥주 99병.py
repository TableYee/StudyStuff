n = int(input())

for i in range(n,0,-1):
    
    if i == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        print("No more bottles of beer on the wall, no more bottles of beer.")
        if n == 1:
            print("Go to the store and buy some more, 1 bottle of beer on the wall.")
        else:
            print("Go to the store and buy some more, {} bottles of beer on the wall.".format(n))
    else:
        print("{} bottles of beer on the wall, {} bottles of beer.".format(i,i))
        if i-1 == 1:
             print("Take one down and pass it around, 1 bottle of beer on the wall.")
        else:
            print("Take one down and pass it around, {} bottles of beer on the wall.".format(i-1))
    print()