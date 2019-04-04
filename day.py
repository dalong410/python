yoil = input("요일을 입력하세요 : ")

if yoil == '월요일' :
    eng = "Monday"
elif yoil == '화요일' :
    eng = "Tuesday"
elif yoil == '수요일' :
    eng = "Wednesday"
elif yoil == '목요일' :
    eng = "thursday"
elif yoil == '금요일' :
    eng = "Friday"
elif yoil == '토요일' :
    eng = "Saturday"
elif yoil == '일요일' :
    eng = "Sunday"
else :
    eng = "incollect"
print(yoil, '은 영어로', eng, '입니다.')