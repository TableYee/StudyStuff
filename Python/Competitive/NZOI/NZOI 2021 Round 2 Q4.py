def chkVowel(seq):
    hasVowel = False
    for i in vowel:
        if i in seq:
            hasVowel = True
    return hasVowel
def chkCons(seq):
    hasCons = False
    for i in vowel:
        if not i in seq:
            hasCons = True
    return hasCons
n = int(input())
l = input()
lst = [i for i in l]
vowel = ['a','e','i','o','u']
ans = 0
search = l[::-1]


if l[n-4:] == 'uack' and (l[0] in vowel or not chkVowel(search[4:])):
    for i in search[4:]:
        if i in vowel: break
        ans+=1    
if l[n-2:] == 'ck' and (not l[0] in vowel or not chkCons(search[2:])):
    for i in search[2:]:
        if not i in vowel: break
        ans+=1

hasVowel = False
for i in vowel:
    if i in l[:n-3]:
        hasVowel = True
if hasVowel:
    for i in range(0,n-3):
        chunk = l[i:i+4]
        if chunk[0] in vowel:
            if chunk[1:4] == 'lf' + chunk[0]:
                ans+=1
                break
            else: break
else:
    if l[n-3:] == 'onk' and n>3:
        ans+=1
    
print(ans)