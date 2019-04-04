rice = 100 * 10000
mouse = 2
day = 0

while rice > 0 :
    day += 1
    if(day % 10 == 0):
        mouse = mouse * 2
    rice = rice - (mouse * 20)


print(day,'일 후', mouse,'마리가 쌀 다 먹었다!!')