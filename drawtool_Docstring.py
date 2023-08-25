
import time
import tkinter
import tkinter.simpledialog
import tkinter.colorchooser
import tkinter.filedialog
from PIL import Image, ImageTk, ImageGrab
from tkinter import colorchooser


def center_window(w, h):
    """set the size of the window

    Args:
        w (interger): the width of the window
        h (interger): the height of the window
    """    
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
thickness=1 #默认画笔粗细为1
foreColor=current_color
def getter(widget):
    """save the image of the chosen area as a JPG file

    Args:
        widget : obtain the width and height of the window

    Notes:
        getter函数:截屏(大小为鼠标选定区域大小长宽各拓宽200像素/若app窗口左上角超出屏幕范围,则从屏幕左上角开始截屏),
                  保存为用户命名的JPG图像(默认保存路径为桌面)
    """    
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
    """create the input text base on the elected spot

    Args:
        event (鼠标事件): the coordinate of the elected spot

    Notes:
        onLeftButtonDown函数:由鼠标左键选择工具栏->文本触发,以鼠标坐标为左上角原点创建文本框等待用户输入内容,
                            文本颜色为当前选定颜色,完成后自动回到自由曲线画笔设置
    """   
    yesno.set(1)
    X.set(event.x)
    Y.set(event.y)
    if what.get() == 4:
        canvas.create_text(event.x, event.y, font=("等线", int(size)), text=text, fill=foreColor,width=thickness)
        what.set(1)


def onLeftButtonMove(event):
    """show the corresponding image according to the chosen button and the movement of the mouse

    Args:
        event (鼠标事件): the current coordinate of the mouse while its left button being held down
    Notes:
        onLeftButtonMove函数:鼠标左键按下移动时，判断当前选择的状态并行使相应功能
                             0:无选择,跳出当前函数
                             1:选择自由曲线(画笔颜色、粗细为用户当前选择)
                             2:选择直线绘制(画笔颜色、粗细为用户当前选择/同时删除创建图形时的画笔轨迹)
                             3:选择矩形绘制(画笔颜色、粗细为用户当前选择/同时删除创建图形时的画笔轨迹)
                             5:选择橡皮擦除(画笔颜色、粗细为用户当前选择/画笔形状为方形,大小为10像素)
                             6:选择椭圆绘制(画笔颜色、粗细为用户当前选择/同时删除创建图形时的画笔轨迹)
    """  
    global lastDraw
    if yesno.get() == 0:
        return
    if what.get() == 1:

        lastDraw = canvas.create_line(X.get(), Y.get(), event.x, event.y,
                                      fill=foreColor,width=thickness)
        X.set(event.x)
        Y.set(event.y)
    elif what.get() == 2:
        try:
            canvas.delete(lastDraw)
        except Exception:
            pass

        lastDraw = canvas.create_line(X.get(), Y.get(), event.x, event.y,
                                      fill=foreColor,width=thickness)
    elif what.get() == 3:

        try:
            canvas.delete(lastDraw)
        except Exception:
            pass
        lastDraw = canvas.create_rectangle(X.get(), Y.get(), event.x, event.y,
                                           outline=foreColor,width=thickness)

    elif what.get() == 5:

        lastDraw = canvas.create_rectangle(event.x - 10, event.y - 10, event.x + 10, event.y + 10,
                                           outline=backColor,width=thickness)
    elif what.get() == 6:

        try:
            canvas.delete(lastDraw)
        except Exception:
            pass
        lastDraw = canvas.create_oval(X.get(), Y.get(), event.x, event.y,
                                      fill=backColor, outline=foreColor,width=thickness)


def onLeftButtonUp(event):
    """create the corresponding image according to the chosen button and the movement of the mouse

    Args:
        event (鼠标事件): the final coordinate of the mouse when its left button releases
    
    Notes:
        onLeftButtonUp函数:鼠标左键松开时,判断当前选择的状态并行使相应功能
                           2:选择直线绘制(画笔颜色、粗细为用户当前选择)
                           3:选择矩形绘制(画笔颜色、粗细为用户当前选择)
                           6:选择椭圆绘制(画笔颜色、粗细为用户当前选择)
                           完成后回到未选择状态
    """  
    global lastDraw
    if what.get() == 2:

        lastDraw = canvas.create_line(X.get(), Y.get(), event.x, event.y, fill=foreColor,width=thickness)
    elif what.get() == 3:

        lastDraw = canvas.create_rectangle(X.get(), Y.get(), event.x, event.y, outline=foreColor,width=thickness)
    elif what.get() == 6:

        lastDraw = canvas.create_oval(X.get(), Y.get(), event.x, event.y, outline=foreColor,width=thickness)
    yesno.set(0)
    end.append(lastDraw)


def onRightButtonUp(event):
    """show rigt-click menu base on the elected spot

    Args:
        event (鼠标事件): the coordinate of the mouse when its right button is clicked

    Notes:
        onRightButtonUp函数:鼠标右键点击结束在附近显示功能菜单
    """ 
    menu.post(event.x_root, event.y_root)

canvas.bind('<Button-1>', onLeftButtonDown)
canvas.bind('<B1-Motion>', onLeftButtonMove)
canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
canvas.bind('<ButtonRelease-3>', onRightButtonUp)
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)


menu = tkinter.Menu(app, bg="red")
app.config(menu=menu)


def Open():
    """import external image based on the default spot and size

    Notes:
       Open函数:导入指定本地图片,调整为指定大小(800,600),以指定坐标(400,300)为左上角原点插入
    """ 
    filename = tkinter.filedialog.askopenfilename(title='导入图片',
                                                  filetypes=[('image', '*.jpg *.png *.gif')])
    if filename:
        global image

        image = Image.open(filename)
        image = image.resize((800, 600), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        canvas.create_image(400, 300, image=image)

def Save():
    """save the canvas
    """
    getter(canvas)

def Clear():
    """clear the canvas
    """ 
    global lastDraw, end
    for item in canvas.find_all():
        canvas.delete(item)
    end = [0]
    lastDraw = 0

def Back():
    """cancel the latest image created on the canvas
    """
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
    """set the choice of "曲线" to 1
    """ 
    what.set(1)

def drawLine():
    """set the choice of "直线" to 2
    """  
    what.set(2)

def drawRectangle():
    """set the choice of "draw rectangle" to 3
    """ 
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


def chooseThickness():
        global thickness
        thickness = tkinter.simpledialog.askinteger('输入画笔粗细', prompt='', initialvalue=1)
        if thickness is None:
                thickness = "1"


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
