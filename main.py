from tkinter import *
import os
import re
win=Tk()
win.title("计算器")
filename = 'record.txt'

def num(a):
  val=result.get()
  result.delete(0,END)
  result.insert(0,val + a)

def clear():
  result.delete(0,END)

def back():
  val=result.get()
  if(len(val)):
    result.delete(len(val)-2,END)
    result.config(text=val[0:len(val)-2])

def calculate():
  expression =result.get()
  try:
    res = eval(expression)
    result.delete(0, END)
    result.insert(0, str(res))
    lines = []
    lines.append(expression+"="+str(res))
    save(lines)
  except:
    result.delete(0, END)
    result.insert(0, "Error")

def save(lst):
    try:
      stu_write = open(filename, 'a', encoding='UTF-8')
    except:
      stu_write = open(filename, 'w', encoding='UTF-8')
    for i in lst:
      stu_write.write(str(i) + '\n')
    stu_write.close()

def show():
  if os.path.exists(filename):
    with open(filename, 'r', encoding='UTF-8') as r_file:
      stu = r_file.readlines()  # 打开文件并逐行读取内容
      record.insert(INSERT,stu)


def char(a):
  val = result.get()
  result.delete(0, END)
  result.insert(0, val + a)


win.geometry("600x500")
win.configure(bg="white")
win.maxsize(600,500)

result=Entry(win,width=300,relief="solid",justify="center",font="Times 18 bold")
result.place(width=300,height=125,x=0,y=0)
record=Text(win,relief="solid",font="Times 8 bold")
record.place(width=300,height=470,x=300,y=30)

butrecord=Button(win,text="查看历史记录",font="Times 12 bold",relief="groove",command=show).place(width=300,height=30,x=300,y=0)
left=Button(win,text="(",font="Times 18 bold",relief="groove",command=lambda: char("(")).place(width=75,height=75,x=0,y=125)
right=Button(win,text=")",font="Times 18 bold",relief="groove",command=lambda: char(")")).place(width=75,height=75,x=75,y=125)

dot=Button(win,text=".",font="Times 18 bold",relief="groove").place(width=75,height=75,x=75,y=425)
equal=Button(win,text="=",font="Times 18 bold",relief="groove",command=calculate).place(width=75,height=75,x=150,y=425)
plus=Button(win,text="+",font="Times 18 bold",relief="groove",command=lambda:char("+")).place(width=75,height=75,x=225,y=200)
minus=Button(win,text="-",font="Times 18 bold",relief="groove",command=lambda:char("-")).place(width=75,height=75,x=225,y=275)
multiply=Button(win,text="×",font="Times 18 bold",relief="groove",command=lambda:char("*")).place(width=75,height=75,x=225,y=350)
divide=Button(win,text="÷",font="Times 18 bold",relief="groove",command=lambda:char("/")).place(width=75,height=75,x=225,y=425)

back=Button(win,text="←",font="Times 18 bold",relief="groove",command=back).place(width=75,height=75,x=225,y=125)
clear=Button(win,text="clear",font="Times 18 bold",relief="groove",command=clear).place(width=75,height=75,x=150,y=125)

btn0=Button(win,text="0",font="Times 18 bold",relief="groove",command=lambda: num("0")).place(width=75,height=75,x=0,y=425)
btn1=Button(win,text="1",font="Times 18 bold",relief="groove",command=lambda: num("1")).place(width=75,height=75,x=0,y=350)
btn2=Button(win,text="2",font="Times 18 bold",relief="groove",command=lambda: num("2")).place(width=75,height=75,x=75,y=350)
btn3=Button(win,text="3",font="Times 18 bold",relief="groove",command=lambda: num("3")).place(width=75,height=75,x=150,y=350)
btn4=Button(win,text="4",font="Times 18 bold",relief="groove",command=lambda: num("4")).place(width=75,height=75,x=0,y=275)
btn5=Button(win,text="5",font="Times 18 bold",relief="groove",command=lambda: num("5")).place(width=75,height=75,x=75,y=275)
btn6=Button(win,text="6",font="Times 18 bold",relief="groove",command=lambda: num("6")).place(width=75,height=75,x=150,y=275)
btn7=Button(win,text="7",font="Times 18 bold",relief="groove",command=lambda: num("7")).place(width=75,height=75,x=0,y=200)
btn8=Button(win,text="8",font="Times 18 bold",relief="groove",command=lambda: num("8")).place(width=75,height=75,x=75,y=200)
btn9=Button(win,text="9",font="Times 18 bold",relief="groove",command=lambda: num("9")).place(width=75,height=75,x=150,y=200)

win.mainloop()


