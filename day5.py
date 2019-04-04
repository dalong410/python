'''
americano = 2000
latte = 3000
cappuccino = 3500

a_num = int(input("Americano? "))
l_num = int(input("Latte? "))
c_num = int(input("Cappuccino? "))

list_cnt = input("Americano, Latte, Cappuccino? ").split()
a_num = list_cnt[0]
l_num = list_cnt[1]
c_num = list_cnt[2]

sum = americano * int(a_num) + latte * int(l_num) + cappuccino * int(c_num)
print("Total : ", int(sum))

#print('americano : {0}, latte: {1}, cappuccino: {2} , sum: {3}'.format(int(input("Americano? ")), int(input("Latte? "))), c_num = int(input("Cappuccino? "), 2000*{0}})

#print("{} {} {} {} {}".format(input('name:'),input('age:'),input('HP:'),input('addr:'),input('sex:')))

#print("{} {} {} {} {}".format(input('name,age,hp,addr,sex').split()))

sum = 0
list_cnt = input("enter 4 numbers? ").split()
for i in range(len(list_cnt)) :
    list_cnt[i] = int(list_cnt[i])
    sum = sum + list_cnt[i]
print('num1 : {0}, num2: {1}, num3: {2} , num4: {3}, sum : {4}, avg : {5}'.format(int(list_cnt[0]), int(list_cnt[1]), int(list_cnt[2]), int(list_cnt[3]), sum, float(sum/4)))

weight = float(input("weight? "))
height = float(input("height? "))
BMI = weight / (height*height)
print(BMI)

x = input("weight?height?").split()
print("BMI : {0}".format(round(int(x[0])/(int(x[1])*int(x[1])), 5)))

output_a = "{:d}".format(52)

output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print(output_a,'\n', output_b,'\n', output_c,'\n', output_d,'\n', output_e)

number = int(input("정수입력>"))
if number > 0:
    print("양수입니다")
if number < 0:
    print("음수입니다")
if number == 0:
    print("0입니다")

number = int(input("정수입력>"))
na = number%2

if na == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

    
number = input("정수입력>")
na = int(number[-1])

if (na == 1 or na == 3 or na == 5 or na == 7 or na == 9):
    print("홀수입니다")
else:
    print("짝수입니다")

yoil = input("요일을 입력하세요 : ")

if (yoil == '월요일') :
    eng = "Monday"
elif  (yoil == '화요일') :
    eng = "Tuesday"
elif (yoil == '수요일') :
    eng = "Wednesday"
elif (yoil == '목요일') :
    eng = "thursday"
elif (yoil == '금요일') :
    eng = "Friday"
elif (yoil == '토요일') :
    eng = "Saturday"
elif (yoil == '일요일') :
    eng = "Sunday"
else :
    eng = "incollect"
print(eng)'''

import datetime
now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))