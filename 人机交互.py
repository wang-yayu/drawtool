import tkinter

def center_window(w, h):
    app.winfo_screenwidth() 
    app.winfo_screenheight() #设置界面长和宽
    app.geometry('%dx%d'% (w, h)) #界面在屏幕中放置位置

app = tkinter.Tk()
app.title('计算器') #app名称
x = 300
y = 400   #计算器长300，高400
center_window(x, y)

app.mainloop()