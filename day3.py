#review
'''
name = input("what is ur name? ")
age = int(input("how old are u? "))
print("Hello,",name,"!!")
print(name,"is",age,"years old")'''

############################################################
'''
##SWICH!
num1 = int(input("input first number : "))
num2 = int(input("input second number : "))

#swich 1
num1, num2 = num2, num1
print("SWICH num1 and num2")
print("new num1 : ",num1)
print("new num2 : ",num2)

#swich 2
tmp = num1
num1 = num2
num2 = tmp
print("SWICH num1 and num2 again!!!")
print("new num1 : ",num1)
print("new num2 : ",num2)

#swich 3
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("SWICH num1 and num2 again2!!!")
print("new num1 : ",num1)
print("new num2 : ",num2)
'''

a = 2 #int(input("input first number : "))
b = 6 #int(input("input second number : "))
sum = a+b
print("sum : ",sum)
minus = a-b
print("minus : ",minus)
mult = a*b
print("mult : ",mult)
div = a/b
print("div : ",div)

#문자열 슬라이싱 & 인덱싱
#슬라이싱 : 문자열 값을 나누어 출력한다
#인덱싱 : 문자열 값을 자리번호를 지정한다(파이썬은 zero index 방식 사용)
val1 = "Strings in Python"
val2 = len(val1)

print(val2)


Ugly = "Beautiful"
Beautiful = "Ugly"
Handsome = Ugly
print("Beautiful")

print(Ugly)

print(Handsome)


