from tkinter import *

root=Tk()

l = {'':0,'I':1,'II':2, 'III':3, 'IV':4, 'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9,'X':10, 'XX':20,'XXX':30, 'XL':40,'L':50, 'LX':60, 'LXX':70, 'LXXX':80, 'XC':90,'c':100,'cc':200,'ccc':300,'cd':400,'d':500,'dc':600,'dcc':700,'dccc':800,'cm':900,'m':1000,'mm':2000,'mmm':3000,'_IV':4000,'_V':5000,'_VM':6000,'_VMM':7000,'_VMMM':8000,'_IX':9000,'_X':10000,'_XX':20000,'_XXX':30000,'_XL':40000, '_L':50000,'_LX':60000,'_LXX':70000,'_LXXX':80000,'_XC':90000}

def get(x):
    l1 = list(l.keys())
    l12= list(l.values())
    return l1[l12.index(x)]

def calc(NUM):
    NUM=str(NUM)
    M=pow(10,len(NUM)-1)
    list = []
    for i in range (0,len(NUM)):
        KEY=int(NUM[i])*M
        M  = M // 10
        if KEY==0:
            continue
        else:
            list.append(get(KEY))
    return list

def click(event):
    global sv
    text = event.widget.cget("text")

    if text == "=":
        value = calc(screen.get())
        sv.set(value)
        screen.update()

    elif text == "c":
        sv.set("")

    else:
        sv.set(sv.get()+text)
        screen.update()

root.title("ROMAN NUMBER CONVERTER")
root.geometry("350x500+800+50")
root.config(bg="white")

CALCULATOR = Label(root,text="ROMAN NO. CONVERTER",font=("times new roman",13,"bold"),bg="#087587",fg="white")
CALCULATOR.place(x=50,y=50,width=250,height=50)

sv = StringVar()
sv.set("")

screen = Entry(root,textvar=sv,font=("times new roman",15,"bold"),bg="yellow",fg="black")
screen.place(x=50,y=120,width=250,height=50)

B1 = Button(root,text="1",font=("times new roman",20,"bold"),bg="#087587",fg="white")
B1.place(x=50,y=200,width=60,height=50)
B1.bind("<Button-1>",click)

B2 = Button(root,text="2",font=("times new roman",20,"bold"),bg="#087587",fg="white")
B2.place(x=140,y=200,width=70,height=50)
B2.bind("<Button-1>",click)

B3 = Button(root,text="3",font=("times new roman",20,"bold"),bg="#087587",fg="white")
B3.place(x=240,y=200,width=60,height=50)
B3.bind("<Button-1>",click)

B4 = Button(root,text="4",font=("times new roman",20,"bold"),bg="#087587",fg="white")
B4.place(x=50,y=250,width=60,height=50)
B4.bind("<Button-1>",click)

B5 = Button(root,text="5",font=("times new roman",20,"bold"),bg="#087587",fg="white")
B5.place(x=140,y=250,width=70,height=50)
B5.bind("<Button-1>",click)

B6 = Button(root,text="6",font=("times new roman",20,"bold"),bg="#087587",fg="white")
B6.place(x=240,y=250,width=60,height=50)
B6.bind("<Button-1>",click)

B7 = Button(root,text="7",font=("times new roman",20,"bold"),bg="#087587",fg="white")
B7.place(x=50,y=320,width=60,height=50)
B7.bind("<Button-1>",click)

B8 = Button(root,text="8",font=("times new roman",20,"bold"),bg="#087587",fg="white")
B8.place(x=140,y=320,width=70,height=50)
B8.bind("<Button-1>",click)

B9 = Button(root,text="9",font=("times new roman",20,"bold"),bg="#087587",fg="white")
B9.place(x=240,y=320,width=60,height=50)
B9.bind("<Button-1>",click)

B0 = Button(root,text="0",font=("times new roman",20,"bold"),bg="#087587",fg="white")
B0.place(x=50,y=390,width=60,height=50)
B0.bind("<Button-1>",click)

EB = Button(root,text="c",font=("times new roman",20,"bold"),bg="#087587",fg="white")
EB.place(x=140,y=390,width=70,height=50)
EB.bind("<Button-1>",click)

BC = Button(root,text="=",font=("times new roman",20,"bold"),bg="#087587",fg="white")
BC.place(x=240,y=390,width=60,height=50)
BC.bind("<Button-1>",click)

root.mainloop()
