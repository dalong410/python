print("버스킹~ 로빈~스 31")
user = 1
num_1list = [i+1 for i in range(31)]
j = 0
while num_1list[0] != 31 or len(num_1list) != 0:
    num = num_1list[0]    
    num = int(input('USER is {}.- enter numbers.'.format(user)))
    if(num == 0):
        user += 1
    else:
        if(num > 3):
            user = user
        else:
            user += 1
            if(num >= len(num_1list)):
                break
            else :
                for j in range(num):
                    del(num_1list[0])
            print(num_1list)

        
    
print("30까지 외쳤습니다. 게임이 끝났네요.")
