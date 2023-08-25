
import time
import tkinter
import tkinter.simpledialog
import tkinter.colorchooser
import tkinter.filedialog
from PIL import Image, ImageTk, ImageGrab
from tkinter import colorchooser


def center_window(w, h):
    app.winfo_screenwidth()
    app.winfo_screenheight()
    app.geometry('%dx%d' % (w, h))


app = tkinter.Tk()
app.title('画图')

x = 1200
y = 800
center_window(x, y)
app.geometry("1200x800+0+0")

yesno = tkinter.IntVar(value=0)
what = tkinter.IntVar(value=1)
X = tkinter.IntVar(value=0)
Y = tkinter.IntVar(value=0)

backColor = '#FFFFFF'

image = tkinter.PhotoImage()
canvas = tkinter.Canvas(app, bg='white', width=x, height=y)
canvas.create_image(x, y, image=image)

lastDraw = 0
end = [0]


current_color=['#000000'] #用于储存当前选中的颜色
thickness=30 #默认画笔粗细为3
foreColor=current_color
def getter(widget):
    time.sleep(0.5)
    x = app.winfo_x() + widget.winfo_x()+15
    y = app.winfo_y() + widget.winfo_y()
    if app.winfo_x() < 0:
        x = 0
    if app.winfo_y() < 0:
        y = 0
    x1 = x + widget.winfo_screenwidth() +200
    y1 = y + widget.winfo_screenheight() +200
    filename = tkinter.filedialog.asksaveasfilename(filetypes=[('.jpg', 'JPG')],
                                                    initialdir='C:\\Users\\lin042\\Desktop\\')
    ImageGrab.grab().crop((x, y, x1, y1)).save(filename)


def onLeftButtonDown(event):
    yesno.set(1)
    X.set(event.x)
    Y.set(event.y)
    if what.get() == 4:
        canvas.create_text(event.x, event.y, font=("等线", int(thickness)), text=text, fill=foreColor)
        what.set(1)


def onLeftButtonMove(event):
    global lastDraw
    if yesno.get() == 0:
        return
    if what.get() == 1:

        lastDraw = canvas.create_line(X.get(), Y.get(), event.x, event.y,
                                      fill=foreColor)
        X.set(event.x)
        Y.set(event.y)
    elif what.get() == 2:
        try:
            canvas.delete(lastDraw)
        except Exception:
            pass

        lastDraw = canvas.create_line(X.get(), Y.get(), event.x, event.y,
                                      fill=foreColor)
    elif what.get() == 3:

        try:
            canvas.delete(lastDraw)
        except Exception:
            pass
        lastDraw = canvas.create_rectangle(X.get(), Y.get(), event.x, event.y,
                                           outline=foreColor)

    elif what.get() == 5:

        lastDraw = canvas.create_rectangle(event.x - 10, event.y - 10, event.x + 10, event.y + 10,
                                           outline=backColor)
    elif what.get() == 6:

        try:
            canvas.delete(lastDraw)
        except Exception:
            pass
        lastDraw = canvas.create_oval(X.get(), Y.get(), event.x, event.y,
                                      fill=backColor, outline=foreColor)


def onLeftButtonUp(event):
    global lastDraw
    if what.get() == 2:

        lastDraw = canvas.create_line(X.get(), Y.get(), event.x, event.y, fill=foreColor)
    elif what.get() == 3:

        lastDraw = canvas.create_rectangle(X.get(), Y.get(), event.x, event.y, outline=foreColor)
    elif what.get() == 6:

        lastDraw = canvas.create_oval(X.get(), Y.get(), event.x, event.y, outline=foreColor)
    yesno.set(0)
    end.append(lastDraw)


def onRightButtonUp(event):
    menu.post(event.x_root, event.y_root)

canvas.bind('<Button-1>', onLeftButtonDown)
canvas.bind('<B1-Motion>', onLeftButtonMove)
canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
canvas.bind('<ButtonRelease-3>', onRightButtonUp)
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)


menu = tkinter.Menu(app, bg="red")
app.config(menu=menu)


def Open():
    filename = tkinter.filedialog.askopenfilename(title='导入图片',
                                                  filetypes=[('image', '*.jpg *.png *.gif')])
    if filename:
        global image

        image = Image.open(filename)
        image = image.resize((800, 600), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        canvas.create_image(400, 300, image=image)

def Save():
    getter(canvas)

def Clear():
    global lastDraw, end
    for item in canvas.find_all():
        canvas.delete(item)
    end = [0]
    lastDraw = 0

def Back():
    global end
    try:
        for i in range(end[-2], end[-1] + 1):
            canvas.delete(i)
        end.pop()
    except:
        end = [0]

menu.add_command(label='导入', command=Open)
menu.add_command(label='撤销', command=Back)
menu.add_command(label='保存', command=Save)
menu.add_command(label='清屏', command=Clear)

menuType = tkinter.Menu(menu, tearoff=0)
menuType2 = tkinter.Menu(menu, tearoff=0)

def drawCurve():
    what.set(1)

def drawLine():
    what.set(2)

def drawRectangle():
    what.set(3)

def drawCircle():
    what.set(6)

def drawText():
    global text, size
    text = tkinter.simpledialog.askstring(title='输入文本', prompt='')
    if text is not None:
        size = tkinter.simpledialog.askinteger('输入字号', prompt='', initialvalue=20)
        if size is None:
            size = "20"
    what.set(4)

def onErase():
    what.set(5)

def chooseBackColor():
    global backColor
    backColor = tkinter.colorchooser.askcolor()[1]

def chooseColor():
    s = colorchooser.askcolor(color="black", title="选择画笔颜色")  # 返回一个tuple,index为1时为颜色的十六进制值
    current_color[0] = s[1]

def savethickness(scale):
    global thickness
    thickness=scale
    print(thickness)
def chooseThickness():

   top=tkinter.Toplevel()
   top.geometry("150x150")
   scale=tkinter.Scale(top,from_=20,to=50,resolution=1,orient="horizontal").pack()
   but=tkinter.Button(top,text='确定',font=20,command=savethickness(scale)).place(width=50,height=40,x=40,y=100)


menuType.add_command(label='铅笔', command=drawCurve)
menuType.add_command(label='直线', command=drawLine)
menuType.add_command(label='矩形', command=drawRectangle)
menuType.add_command(label='圆形', command=drawCircle)
menuType.add_command(label='文本', command=drawText)
menuType.add_command(label='橡皮擦', command=onErase)
menuType.add_separator()
menuType.add_command(label='选择背景色', command=chooseBackColor)
menu.add_cascade(label='工具栏', menu=menuType)
menu.add_cascade(label='画笔选项', menu=menuType2)
menuType2.add_command(label='画笔颜色', command=chooseColor)
menuType2.add_command(label='画笔粗细', command=chooseThickness)

app.mainloop()
