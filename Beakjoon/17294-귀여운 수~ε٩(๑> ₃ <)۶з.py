k = int(input())
lst = []

for i in str(k):
    lst.append(int(i))
if len(lst) != 1:
    sum = lst[0] - lst[1]
else:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    quit()

for i in range(1,len(lst)-1):
    if lst[i] - lst[i+1] != sum:
        print("흥칫뿡!! <(￣ ﹌ ￣)>")
        quit()
print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    