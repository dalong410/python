'''import datetime
now = datetime.datetime.now()

if now.hour < 12 :
    print("AM")
else :
    print("PM")

month = int(input('월을 입력해주세요 : '))
if 3 <= month <=5 :
    weather = '봄'
elif 6 <= month <=8 :
    weather = '여름'
elif 9 <= month <=11 :
    weather = '가을'
elif month == 12 or month <= 2 :
    weather = '겨울'
print(month, '월은', weather, '입니다')

gpa = float(input('학점을 입력해주세요 : '))

if gpa == 4.5 :
    state = '신'
elif gpa >= 4.2 :
    state = '교수님의 사랑'
elif gpa >= 3.5 :
    state = '현 체제의 수호자'
elif gpa >= 2.8 :
    state = '일반인'
elif gpa >= 2.3 :
    state = '일탈을 꿈꾸는 소시민'
elif gpa >= 1.75 :
    state = '오락문화의 선구자'
elif gpa >= 1 :
    state = '불가촉천민'
elif gpa >= 0.5 :
    state = '자벌레'
elif gpa > 0 :
    state = '플랑크톤'
else :
    state = '시대를 앞서가는 혁명의 씨앗'

print(state)

score1 = float(input('심판1 : '))
score2 = float(input('심판2 : '))
score3 = float(input('심판3 : '))
score4 = float(input('심판4 : '))
score5 = float(input('심판5 : '))

max_score = max(score1, score2, score3, score4, score5)
min_score = min(score1, score2, score3, score4, score5)
sum_score = score1 + score2 + score3 + score4 + score5
avg_sum = sum_score - max_score - min_score
avg = avg_sum / 3
print(avg)'''

ps = input('4자리 암호를 입력해주세요 : ').split()
ps1 = int(ps[0])
ps2 = int(ps[1])
ps3 = int(ps[2])
ps4 = int(ps[3])

if ps2 == ps1 + 1 or ps3 == ps2 + 1 or ps4 == ps3 + 1 :
    print('사용할 수 없는 암호입니다.')
elif ps2 == ps1 - 1 or ps3 == ps2 - 1 or ps4 == ps3 - 1 :
    print('사용할 수 없는 암호입니다.')
elif ps1 == ps2 or ps1 == ps3 or ps1 == ps4 or ps2 == ps3 or ps2 == ps4 or ps3 == ps4 :
    print('사용할 수 없는 암호입니다.')
else :
    print('사용할 수 있는 암호입니다.')