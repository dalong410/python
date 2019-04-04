# GUI진법 변환기 - 이지영

from tkinter import *

# 2진수를 10진수로 변환하는 함수
def binary_decimal(innum):
    innum = str(innum)
    length = len(innum) - 1
    outD = 0
    for index in innum:
        outD += int(index) * (2 ** length)
        length -= 1
    return outD
 
# 16진수를 10진수로 변환하는 함수   
def hex_decimal(innum):
    innum = str(innum)
    length = len(innum) - 1
    outD = 0
    for index in innum:
        if index >= 'A' and index <= 'F':
            outD += (ord(index) - 55) * (16 ** length)
        else:
            outD += int(index) * (16 ** length)
        length -= 1
    return outD

# 10진수를 2진수로 변환하는 함수
def decimal_binary(innum):
    innum = int(innum)
    outB = ''
    while innum > 0:
        outB = str(innum % 2) + outB
        innum //= 2
    return outB

# 10진수를 16진수로 변환하는 함수
def decimal_hex(innum):
    innum = int(innum)
    outX = ''
    while innum > 0:
        rem = innum % 16
        if rem >= 10:
            outX = chr(rem+55) + outX
        else:
            outX = str(rem) + outX
        innum //= 16
    return outX

# 숫자버튼 클릭 함수
def numClick(num):
    inText.insert(END, num)

# 변환버튼 클릭 함수
def cvtClick(base):
    inbase = int(rdoBase.get())
    outbase = int(base)
    innum = inText.get()
    
    if inbase == 2:
        outD = binary_decimal(innum)
    elif inbase == 10:
        outD = innum
    elif inbase == 16:
        outD = hex_decimal(innum)

    if outbase == 2:
        outB = '0b' + decimal_binary(outD)
        outText.delete(0, END)
        outText.insert(0, outB)
    elif outbase == 10:
        outText.delete(0, END)
        outText.insert(0, outD)
    elif outbase == 16:
        outX = '0x' + decimal_hex(outD)
        outText.delete(0, END)
        outText.insert(0, outX)

# 창 생성
root = Tk()
root.title('진법 변환기')

# 진법을 선택하는 라디오 버튼 생성
rdoFrame = Frame(root)
rdoFrame.pack(pady=5)
rdoBase = StringVar()
info = ['2', '10', '16']
for base in info:
    rdo = Radiobutton(rdoFrame, text=base+'진수',
                      variable=rdoBase, value=base)
    rdo.pack(side=LEFT)

# 입력란 생성
inText = Entry(root)
inText.insert(0, '')
inText.pack(pady=5)

# 숫자 버튼 생성
numFrame = Frame(root)
numFrame.pack(pady=5)
buttons = ['7410', '852 ', '963 ', 'ECA ', 'FDB ']
for col in buttons:
    frm=Frame(numFrame)
    frm.pack(side=LEFT)
    for row in col:
        if row != ' ':
            numBtn = Button(frm, text=row,
                            command=(lambda char=row: numClick(char)))
        else:
            numBtn = Button(frm, state='disabled', borderwidth = 0)
        numBtn.pack(ipadx=2, padx=3, pady=3)

# 변환 버튼 생성
cvtFrame = Frame(root)
cvtFrame.pack(pady=5)
for base in info:
    cvtBtn = Button(cvtFrame, text=base+'진수',
                    command=(lambda char=base: cvtClick(char)))
    cvtBtn.pack(side=LEFT)

# 출력란 생성
outText = Entry(root)
outText.insert(0, '')
outText.pack(pady=5)

root.mainloop()
