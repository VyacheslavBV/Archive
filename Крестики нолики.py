import tkinter as tk
w=tk.Tk()
w.geometry("240x278")
q=s1=s2=s3=s4=s5=s6=s7=s8=s9=0
c1=c2=c3=c4=c5=c6=c7=c8=c9=0
o=tk.Entry(width=35)
o.place(x=0)
def f():
    a1 = tk.Label(text="", width=10, height=5, bg="black")
    a1.place(x=0, y=20)
    a2 = tk.Label(text="", width=10, height=5, bg="black")
    a2.place(x=80, y=20)
    a3 = tk.Label(text="", width=10, height=5, bg="black")
    a3.place(x=160, y=20)
    a4 = tk.Label(text="", width=10, height=5, bg="black")
    a4.place(x=0, y=106)
    a5 = tk.Label(text="", width=10, height=5, bg="black")
    a5.place(x=80, y=106)
    a6 = tk.Label(text="", width=10, height=5, bg="black")
    a6.place(x=160, y=106)
    a7 = tk.Label(text="", width=10, height=5, bg="black")
    a7.place(x=0, y=192)
    a8 = tk.Label(text="", width=10, height=5, bg="black")
    a8.place(x=80, y=192)
    a9 = tk.Label(text="", width=10, height=5, bg="black")
    a9.place(x=160, y=192)
def sr():
    global f,s1,s2,s3,s4,s5,s6,s7,s8,s9
    if s1==s2==s3==1:
        f()
        o.insert(0,"Победил Красный игрок!")
    elif s4==s5==s6==1:
        f()
        o.insert(0,"Победил Красный игрок!")
    elif s7==s8==s9==1:
        f()
        o.insert(0,"Победил Красный игрок!")
    elif s1==s4==s7==1:
        f()
        o.insert(0,"Победил Красный игрок!")
    elif s2==s5==s8==1:
        f()
        o.insert(0,"Победил Красный игрок!")
    elif s3==s6==s9==1:
        f()
        o.insert(0,"Победил Красный игрок!")
    elif s1==s5==s9==1:
        f()
        o.insert(0,"Победил Красный игрок!")
    elif s3==s5==s7==1:
        f()
        o.insert(0,"Победил Красный игрок!")
def cr():
    global f,c1,c2,c3,c4,c5,c6,c7,c8,c9
    if c1==c2==c3==1:
        f()
        o.insert(0,"Победил Синий игрок!")
    elif c4==c5==c6==1:
        f()
        o.insert(0,"Победил Синий игрок!")
    elif c7==c8==c9==1:
        f()
        o.insert(0,"Победил Синий игрок!")
    elif c1==c4==c7==1:
        f()
        o.insert(0,"Победил Синий игрок!")
    elif c2==c5==c8==1:
        f()
        o.insert(0,"Победил Синий игрок!")
    elif c3==c6==c9==1:
        f()
        o.insert(0,"Победил Синий игрок!")
    elif c1==c5==c9==1:
        f()
        o.insert(0,"Победил Синий игрок!")
    elif c3==c5==c7==1:
        f()
        o.insert(0,"Победил Синий игрок!")
def b1():
    global b1,q,s1,c1,cr,sr
    del(b1)
    q=q+1
    if q%2==0:
        a1=tk.Label(text="",width=10,height=5,bg="red")
        s1=1
        a1.place(x=0,y=20)
    else:
        a1 = tk.Label(text="", width=10, height=5, bg="blue")
        c1=1
        a1.place(x=0,y=20)
    sr()
    cr()
def b2():
    global b2,q,s2,c2,cr,sr
    del(b2)
    q=q+1
    if q%2==0:
        a2=tk.Label(text="",width=10,height=5,bg="red")
        s2=1
        a2.place(x=80,y=20)
    else:
        a2 = tk.Label(text="", width=10, height=5, bg="blue")
        c2=1
        a2.place(x=80,y=20)
    sr()
    cr()
def b3():
    global b3,q,s3,c3,cr,sr
    del(b3)
    q=q+1
    if q%2==0:
        a3=tk.Label(text="",width=10,height=5,bg="red")
        s3=1
        a3.place(x=160,y=20)
    else:
        a3 = tk.Label(text="", width=10, height=5, bg="blue")
        c3=1
        a3.place(x=160,y=20)
    sr()
    cr()
def b4():
    global b4,q,s4,c4,cr,sr
    del(b4)
    q=q+1
    if q%2==0:
        a4=tk.Label(text="",width=10,height=5,bg="red")
        s4=1
        a4.place(x=0,y=106)
    else:
        a4 = tk.Label(text="", width=10, height=5, bg="blue")
        c4=1
        a4.place(x=0,y=106)
    sr()
    cr()
def b5():
    global b5,q,s5,c5,cr,sr
    del(b5)
    q=q+1
    if q%2==0:
        a5=tk.Label(text="",width=10,height=5,bg="red")
        s5=1
        a5.place(x=80,y=106)
    else:
        a5 = tk.Label(text="", width=10, height=5, bg="blue")
        c5=1
        a5.place(x=80,y=106)
    sr()
    cr()
def b6():
    global b6,q,s6,c6,cr,sr
    del(b6)
    q=q+1
    if q%2==0:
        a6=tk.Label(text="",width=10,height=5,bg="red")
        s6=1
        a6.place(x=160,y=106)
    else:
        a6 = tk.Label(text="", width=10, height=5, bg="blue")
        c6=1
        a6.place(x=160,y=106)
    sr()
    cr()
def b7():
    global b7,q,s7,c7,cr,sr
    del(b7)
    q=q+1
    if q%2==0:
        a7=tk.Label(text="",width=10,height=5,bg="red")
        s7=1
        a7.place(x=0,y=192)
    else:
        a7 = tk.Label(text="", width=10, height=5, bg="blue")
        c7=1
        a7.place(x=0,y=192)
    sr()
    cr()
def b8():
    global b8,q,s8,c8,cr,sr
    del(b8)
    q=q+1
    if q%2==0:
        a8=tk.Label(text="",width=10,height=5,bg="red")
        s8=1
        a8.place(x=80,y=192)
    else:
        a8 = tk.Label(text="", width=10, height=5, bg="blue")
        c8=1
        a8.place(x=80,y=192)
    sr()
    cr()
def b9():
    global b9,q,s9,c9,cr,sr
    del(b9)
    q=q+1
    if q%2==0:
        a9=tk.Label(text="",width=10,height=5,bg="red")
        s9=1
        a9.place(x=160,y=192)
    else:
        a9 = tk.Label(text="", width=10, height=5, bg="blue")
        c9=1
        a9.place(x=160,y=192)
    sr()
    cr()
b1=tk.Button(text="",width=10,height=5,command=b1)
b2=tk.Button(text="",width=10,height=5,command=b2)
b3=tk.Button(text="",width=10,height=5,command=b3)
b4=tk.Button(text="",width=10,height=5,command=b4)
b5=tk.Button(text="",width=10,height=5,command=b5)
b6=tk.Button(text="",width=10,height=5,command=b6)
b7=tk.Button(text="",width=10,height=5,command=b7)
b8=tk.Button(text="",width=10,height=5,command=b8)
b9=tk.Button(text="",width=10,height=5,command=b9)
b1.place(x=0,y=20)
b2.place(x=80,y=20)
b3.place(x=160,y=20)
b4.place(x=0,y=106)
b5.place(x=80,y=106)
b6.place(x=160,y=106)
b7.place(x=0,y=192)
b8.place(x=80,y=192)
b9.place(x=160,y=192)
def ce():
    global q,s1,s2,s3,s4,s5,s6,s7,s8,s9,c1,c2,c3,c4,c5,c6,c7,c8,c9
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,t1,t2,t3,t4,t5,t6,t7,t8,t9

    def b1():
        global b1, q, s1, c1, cr, sr
        del (b1)
        q = q + 1
        if q % 2 == 0:
            a1 = tk.Label(text="", width=10, height=5, bg="red")
            s1 = 1
            a1.place(x=0, y=20)
        else:
            a1 = tk.Label(text="", width=10, height=5, bg="blue")
            c1 = 1
            a1.place(x=0, y=20)
        sr()
        cr()

    def b2():
        global b2, q, s2, c2, cr, sr
        del (b2)
        q = q + 1
        if q % 2 == 0:
            a2 = tk.Label(text="", width=10, height=5, bg="red")
            s2 = 1
            a2.place(x=80, y=20)
        else:
            a2 = tk.Label(text="", width=10, height=5, bg="blue")
            c2 = 1
            a2.place(x=80, y=20)
        sr()
        cr()

    def b3():
        global b3, q, s3, c3, cr, sr
        del (b3)
        q = q + 1
        if q % 2 == 0:
            a3 = tk.Label(text="", width=10, height=5, bg="red")
            s3 = 1
            a3.place(x=160, y=20)
        else:
            a3 = tk.Label(text="", width=10, height=5, bg="blue")
            c3 = 1
            a3.place(x=160, y=20)
        sr()
        cr()

    def b4():
        global b4, q, s4, c4, cr, sr
        del (b4)
        q = q + 1
        if q % 2 == 0:
            a4 = tk.Label(text="", width=10, height=5, bg="red")
            s4 = 1
            a4.place(x=0, y=106)
        else:
            a4 = tk.Label(text="", width=10, height=5, bg="blue")
            c4 = 1
            a4.place(x=0, y=106)
        sr()
        cr()

    def b5():
        global b5, q, s5, c5, cr, sr
        del (b5)
        q = q + 1
        if q % 2 == 0:
            a5 = tk.Label(text="", width=10, height=5, bg="red")
            s5 = 1
            a5.place(x=80, y=106)
        else:
            a5 = tk.Label(text="", width=10, height=5, bg="blue")
            c5 = 1
            a5.place(x=80, y=106)
        sr()
        cr()

    def b6():
        global b6, q, s6, c6, cr, sr
        del (b6)
        q = q + 1
        if q % 2 == 0:
            a6 = tk.Label(text="", width=10, height=5, bg="red")
            s6 = 1
            a6.place(x=160, y=106)
        else:
            a6 = tk.Label(text="", width=10, height=5, bg="blue")
            c6 = 1
            a6.place(x=160, y=106)
        sr()
        cr()

    def b7():
        global b7, q, s7, c7, cr, sr
        del (b7)
        q = q + 1
        if q % 2 == 0:
            a7 = tk.Label(text="", width=10, height=5, bg="red")
            s7 = 1
            a7.place(x=0, y=192)
        else:
            a7 = tk.Label(text="", width=10, height=5, bg="blue")
            c7 = 1
            a7.place(x=0, y=192)
        sr()
        cr()

    def b8():
        global b8, q, s8, c8, cr, sr
        del (b8)
        q = q + 1
        if q % 2 == 0:
            a8 = tk.Label(text="", width=10, height=5, bg="red")
            s8 = 1
            a8.place(x=80, y=192)
        else:
            a8 = tk.Label(text="", width=10, height=5, bg="blue")
            c8 = 1
            a8.place(x=80, y=192)
        sr()
        cr()

    def b9():
        global b9, q, s9, c9, cr, sr
        del (b9)
        q = q + 1
        if q % 2 == 0:
            a9 = tk.Label(text="", width=10, height=5, bg="red")
            s9 = 1
            a9.place(x=160, y=192)
        else:
            a9 = tk.Label(text="", width=10, height=5, bg="blue")
            c9 = 1
            a9.place(x=160, y=192)
        sr()
        cr()
    q = s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = 0
    c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0
    b1 = tk.Button(text="", width=10, height=5, command=b1)
    b2 = tk.Button(text="", width=10, height=5, command=b2)
    b3 = tk.Button(text="", width=10, height=5, command=b3)
    b4 = tk.Button(text="", width=10, height=5, command=b4)
    b5 = tk.Button(text="", width=10, height=5, command=b5)
    b6 = tk.Button(text="", width=10, height=5, command=b6)
    b7 = tk.Button(text="", width=10, height=5, command=b7)
    b8 = tk.Button(text="", width=10, height=5, command=b8)
    b9 = tk.Button(text="", width=10, height=5, command=b9)
    b1.place(x=0, y=20)
    b2.place(x=80, y=20)
    b3.place(x=160, y=20)
    b4.place(x=0, y=106)
    b5.place(x=80, y=106)
    b6.place(x=160, y=106)
    b7.place(x=0, y=192)
    b8.place(x=80, y=192)
    b9.place(x=160, y=192)
    o.delete(0,1000)
ce=tk.Button(text="ce",command=ce)
ce.place(x=217,y=0)
w.mainloop()