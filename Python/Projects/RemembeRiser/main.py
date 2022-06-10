import pdftotext
import pandas as pd
import sys
import time
PDFfilename = 'vocab.pdf' 
leave = 0

with open(PDFfilename, 'rb') as file:
    fileReader = pdftotext.PDF(file)

def wait(t):
    m,s = t, 0
    
    while s <= t*60:
        print("\r{}분 {}초 남았습니다.".format(m,s))
        sys.stdout.flush()
        time.sleep(1)
        s+=1

def test(lst,d):
    vocab = lst[d+1]
    vocab.shuffle()
    ans,gans = [],[]
    correct = 0

    for eng,kor in vocab:
        ans.append([eng,kor].shuffle())
        gans.append(input("{}의 뜻은 무엇일까요?".format(ans[-1][0])))

    for i in range(len(ans)):
        print("{}.\n".foramt(i+1))
        if ans[i][1] == gans[i]:
            print("{} = {} 맞추셨습니다!".format(ans[i][0],gans[i]))
            correct += 1
        else:
            print("{} != {} 틀리셨습니다..".format(ans[i][0],gans[i]))
            print("정답은 {} = {} 입니다!".format(ans[i][0],ans[i][1]))

    print("맞춘갯수: {}")
    input("엔터를 눌러서 계속합시다!")


day = int(input("원하는 Day를 적어주십시요: "))
f = fileReader[day-1].split()
f = f[1:-1]
print(f)
print("단어 시험을 시작하겠습니다")

while not leave:
    test()
    sys.stdout.flush()
    print("복습시간 10분이 시작됩니다")
    wait(10)
    print('\a')
    sys.stdout.flush()
    print("망각시간 5분이 시작됩니다")
    wait(5)
    print('\a')
    leave = input("계속 하시겠습니까? (0과 1로 답함)")