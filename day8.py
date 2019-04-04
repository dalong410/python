'''
def finddrop(players, start, step):
    drop = (start+step) % len(players)
    return drop

players = int(input("How many player do you want to play??"))
start = int(input("Choose first player!"))
step = int(input("Choose step!"))

players_list = [i for i in range(players)]

while len(players_list) > 1 :
    drop = finddrop(players_list, start, step)
    start = drop - 1
    print("{} bomb!!!".format(players_list[drop]))
    del players_list[drop]

print('last player is', players_list[0])

from random import randint
pc = randint(1, 100)

user = 0
cnt = 0
while user != pc:
    user = int(input("Guess!!!!"))
    if(user > pc) :
        print('down!!')
    else :
        print('up!!')
    cnt += 1

print('PC\'s number is {}.\ntried {} times.'.format(pc, cnt))

def print_string(text, count=1):
    for i in range(count) :
        print(text)

print_string('hello')

def print_personnel(name, position='staff', nationality='Korea'):
    print('name = {0}'.format(name))
    print('position = {0}'.format(position))
    print('nationality = {0}'.format(nationality))

print_personnel('Saebom')
print_personnel('Kim', 'Programmer')
print_personnel('Saebom Kim', 'CEO', 'USA')

def print_team(**players):
    for k in players.keys():
        print('{0} - {1}'.format(k, players[k]))

print_team(카시야스='GK', 호날두='FW', 알론소='MF', 페페='DF')

def print_args(n, *values):
    for i in range(n):
        for value in values:
            print(values[i])
        print()

print_args(3, "1","2", "3")

import tkinter

window = tkinter.Tk()

window.title("Python")
window.geometry("640x400+100+100")
window.resizable(False, False)
#버튼 생성

count = 0
def countplus() :
    global count

    count += 1
    label.config(text=str(count))

label= tkinter.Label(window, text='파이썬', width=10, height=5, fg='red', relief='solid')
label.pack()

button = tkinter.Button(window, text='눌러봐', overrelief="solid", width=15, command=countplus, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()
'''
import tkinter
from math import *

window = tkinter.Tk()

window.title("Python")
window.geometry("640x400+100+100")
window.resizable(False, False)

def calc(event) :
    label.config(text='=result='+str(eval(entry.get())))

entry = tkinter.Entry(window)
entry.bind("<Return>", calc)
entry.pack()

label= tkinter.Label(window)
label.pack()

window.mainloop()