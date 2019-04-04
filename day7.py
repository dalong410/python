import random

num = ["0","0","0"]
user = ["0","0","0"]

num[0] = str(random.randint(1,9))
num[1] = str(random.randint(1,9))
num[2] = str(random.randint(1,9))

strike = 0
ball = 0

user = input('3자리 수를 입력해주세요 : (1~9)').split()

for i in range(len(num)) :
    if (user[i]) == (num[i]) :
        strike += 1
    if ((user[i] in num) and (user[i] != num[i])) :
        ball += 1
print('컴퓨터 랜덤 숫자 : ', num)
print('사용자 입력 숫자 : ', user)
print("Strike :", strike, "Ball : ", ball)

if(strike == 3) :
    print('추카추카')