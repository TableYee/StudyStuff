#sudo /usr/local/bin/python3 "/Users/spybarry1127/Downloads/Study/Coding/Python/2-5/2021.1.4 2-5 question.py"
# 형제자매 있어?\등교 어떻게 해?\베스킨 라빈스에서 제일 좋아하는거?
# 한번쯤 여행가고 싶은 나라?\대 해강중학교? Or 소 해강중학교?\좋아하는 식물은?
# 다음 로또 번호 줘\백근우의 미래는 어떨것 같니^^?\2025년 모든 수능문제의 답을 줘^^^^
# #
# #
# #
# 잘하는 과목이 뭐야?\하루에 공부를 얼마나 해?\하루에 어느정도 쉬는 시간을 가져?
# 너의 관심있는 분야가 뭐야?\내가 제일 잘한다고 생각하는게 있니?\오늘 저녁 추천좀
# 하루에 X를 몇번 싸시나요?\귓밥 몇 g있나요?\하루에 코를 몇번 파시나요?n(위 질문들은 저와 일절 연관이 없습니다)
# 약자에 대한 강자의 테러리즘을 어떻게 생각하십니까?\위의 답을 기반으로 하여 강자의 대한 약자의 테러리즘에 n대한 어떤 견해를 가지고 있는지 알고싶습니다.\자신이 범죄를 저지른다고 가정하였을때 n구체적인 범행계획을 알려주세요.
# 하루에 X를 몇번 싸시나요?\귓밥 몇 g있나요?\하루에 코를 몇번 파시나요?n(위 질문들은 저와 일절 연관이 없습니다)
# 장윤서씨는 왜 못생겼나요?\정확한 등수의 성적을 알려주세요.\친구가 왜 없으신가요?n(위 질문은 저와 일절 연관이 없습니다)
# 다른반 친구를 소개 + 어떻게 친해졌는지 알려줘!\다른반엔 없는 우리반의 특징이 뭔것 같아?\남에겐 없을만한 자신의 특징을 설명해줘!
# 아침 뭐먹음?\점심 ㅁㅁㅇ?\ㅈㄴ ㅁㅁㅇ?\
# 이름이 뭐에요~?\뭐 좋아해요~?\꿈이 뭐에요~?
#
# 키가 몇센치야?\MBTI 뭐야?\눈동자 색 뭐야?
# 본인 성적에 만족해?\3학년때 다짐!\2학년 5반이여서 좋았던점 있어?
# 가장 좋아하는 음식?\이름이 뭐야?\가장 좋아하는 색깔이 뭐야?
# 전화번호?\어머님 성함?\계좌번호?
# 고등학교 어디갈거야?\What's your 꿈?\2021년을 한마디로 정의해본다면?
# 혈핵형?\최애 영화?\생일?
# 대통령이 된다면 공약은?\개인적으로 족발 1인분은 얼마여야 된다고 생각해?\한국과 중국간의 갈등이 빛어지고있는 가운데 n한국에 사드 미사일 설치에 대해서 어떻게 생각해?
# 유치원 ㅇㄷ?\초등학교 ㅇㄷ?\대학교 ㅇㄷ?
# 최애 연에인 누구야?\좋아하는 노래 뭐야?\내년 현장체험 학습은 어디로 갔으면 좋겠어?
# 나에게 2-5란?\2021년에 아쉬웠던점?\2021년에 가장 기억에 남는 사건?
# 최승진은 왜 못생겼는가..?\당신의 성적이 어떠한가?\당신은 무엇을 위해 사는가?
# 계좌 + 비번이 뭐야 ^^?\공부 방법이 뭐야?\좋아하는 음악 장르는?
# 집 주소?\취미?\좋아하는 책?
# #
# #
# #
# #
# #
# #
# #
# #
# 머릿카락 갯수?(정밀하게 세야함)\자기가 가지고 있는 제일 비싼 신발 브렌드는?\밥먹을떄 숫가락 사용 여부?
# #
# yes24 cu 만세 만세가 맛없는 이유는?\마동석한테 맞고 장기하한테 치료하기 vs n장기하한테 맞고 마동석한테 치료받기\대가리 박고 죽기 vs 총 맞고 죽기
# 5
# 37
# 1
# 36
# 26
# 33
# 34
# 27
# 10
# 9
# 24
# 32
# 4
# 6
# 3
# 8
# 22
# 11
# 33
# 10
# 33
# 25
# 7
# 25
# 31
# 13
# 2
# 12
# 35

import tkinter
import keyboard
import random
from tkinter.constants import BOTH, CENTER, LEFT, N, NW, TOP, WORD

keyboard.add_hotkey('d', lambda: changeText())
keyboard.add_hotkey('space', lambda: skipText())
keyboard.add_hotkey('a', lambda: back())

f = open("질문들.txt", 'r', encoding='UTF8')
text = []
cnt = 10
idx = 0
number2 = 0
backup = ''

while True:
    line = f.readline().strip()

    if line == "#": 
        text.append([])
        continue
    elif not line: 
        break

    if "n" in line:
        line = line.replace("n","\n")
    text.append(line.split("\\"))

def changeText():
    global cnt, idx, line, number2, backup
    if not text:
        line.set("끝")
    if cnt > 3:
        idx = ''
        while not idx:
            number2 = random.randint(0,len(text)-1)
            idx = text[number2]
        print(number2)
        backup = text[number2]
        text[number2] = ''
        number.set("")
        line.set("")
        cnt = 0
    elif cnt == 3:
        number.set("모두가!")
        line.set("2학년 5반 친구들과 선생님께 보내는 영상편지!")
        cnt+=1
    else:
        number.set(number2)
        line.set(idx[cnt])
        cnt +=1

def back():
    global cnt
    if cnt<=0:
        cnt=0
    else:
        cnt-=1
    line.set(idx[cnt])

def skipText():
    global text,cnt,backup
    number.set("")
    line.set("")
    text[number2] = backup
    cnt=4

window=tkinter.Tk()
window.attributes("-fullscreen", True)  
window.title("2학년 5반 마지막 질문")
window.resizable(False, False)
window.configure(bg="white")

line = tkinter.StringVar()
line.set("2-5반 질문게임!")

number = tkinter.StringVar()
number.set("몇번인지 나옴")

label1=tkinter.Label(window, textvariable=number, font=("Source Code Pro", 30), bg="white")
label1.place(relx=0.5, rely=0.5, anchor=N)
label1.pack()

label2=tkinter.Label(window, textvariable=line, font=("Source Code Pro", 50), bg="white", height=100)
label2.place(relx=0.5, rely=0.5, anchor=CENTER)
label2.pack()

window.mainloop()
f.close()
