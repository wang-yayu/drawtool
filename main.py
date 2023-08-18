from tkinter import *
win=Tk()
win.title("计算器")

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
  except:
    result.delete(0, END)
    result.insert(0, "Error")

def char(a):
  val = result.get()
  result.delete(0, END)
  result.insert(0, val  + a)


win.geometry("300x500")
win.configure(bg="white")
win.maxsize(300,500)
result=Entry(win,width=300,relief="solid",justify="center")
result.place(width=300,height=125,x=0,y=0)
left=Button(win,text="(",font=14,relief="flat",command=lambda: char("(")).place(width=75,height=75,x=0,y=125)
right=Button(win,text=")",font=14,relief="flat",command=lambda: char(")")).place(width=75,height=75,x=75,y=125)

dot=Button(win,text=".",font=14,relief="flat").place(width=75,height=75,x=75,y=425)
equal=Button(win,text="=",font=14,relief="flat",command=calculate).place(width=75,height=75,x=150,y=425)
plus=Button(win,text="+",font=14,relief="flat",command=lambda:char("+")).place(width=75,height=75,x=225,y=200)
minus=Button(win,text="-",font=14,relief="flat",command=lambda:char("-")).place(width=75,height=75,x=225,y=275)
multiply=Button(win,text="x",font=14,relief="flat",command=lambda:char("*")).place(width=75,height=75,x=225,y=350)
divide=Button(win,text="/",font=14,relief="flat",command=lambda:char("/")).place(width=75,height=75,x=225,y=425)

back=Button(win,text="<-",font=14,relief="flat",command=back).place(width=75,height=75,x=225,y=125)
clear=Button(win,text="clear",font=14,relief="flat",command=clear).place(width=75,height=75,x=150,y=125)

btn0=Button(win,text="0",font=14,relief="flat",command=lambda: num("0")).place(width=75,height=75,x=0,y=425)
btn1=Button(win,text="1",font=14,relief="flat",command=lambda: num("1")).place(width=75,height=75,x=0,y=350)
btn2=Button(win,text="2",font=14,relief="flat",command=lambda: num("2")).place(width=75,height=75,x=75,y=350)
btn3=Button(win,text="3",font=14,relief="flat",command=lambda: num("3")).place(width=75,height=75,x=150,y=350)
btn4=Button(win,text="4",font=14,relief="flat",command=lambda: num("4")).place(width=75,height=75,x=0,y=275)
btn5=Button(win,text="5",font=14,relief="flat",command=lambda: num("5")).place(width=75,height=75,x=75,y=275)
btn6=Button(win,text="6",font=14,relief="flat",command=lambda: num("6")).place(width=75,height=75,x=150,y=275)
btn7=Button(win,text="7",font=14,relief="flat",command=lambda: num("7")).place(width=75,height=75,x=0,y=200)
btn8=Button(win,text="8",font=14,relief="flat",command=lambda: num("8")).place(width=75,height=75,x=75,y=200)
btn9=Button(win,text="9",font=14,relief="flat",command=lambda: num("9")).place(width=75,height=75,x=150,y=200)

win.mainloop()


