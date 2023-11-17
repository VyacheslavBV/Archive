import tkinter as tk
w=tk.Tk()
w.geometry("268x305")
a="Введите число"
o=tk.Entry(width=44)
o.insert(0,a)
o.pack()
Y=""
X=l=q=0
def f1():
    global a,Y,q
    if a=="Введите число":
        a=""
    if q==1:
        Y=Y+"1"
    a=a+"1"
    o.delete(0,10000)
    o.insert(0,a)
def f2():
    global a,Y,q
    if a=="Введите число":
        a=""
    if q==1:
        Y=Y+"2"
    a=a+"2"
    o.delete(0,10000)
    o.insert(0,a)
def f3():
    global a,Y,q
    if a=="Введите число":
        a=""
    if q==1:
        Y=Y+"3"
    a=a+"3"
    o.delete(0,10000)
    o.insert(0,a)
def f4():
    global a,Y,q
    if a=="Введите число":
        a=""
    if q==1:
        Y=Y+"4"
    a=a+"4"
    o.delete(0,10000)
    o.insert(0,a)
def f5():
    global a,Y,q
    if a=="Введите число":
        a=""
    if q==1:
        Y=Y+"5"
    a=a+"5"
    o.delete(0,10000)
    o.insert(0,a)
def f6():
    global a,Y,q
    if a=="Введите число":
        a=""
    if q==1:
        Y=Y+"6"
    a=a+"6"
    o.delete(0,10000)
    o.insert(0,a)
def f7():
    global a,Y,q
    if a=="Введите число":
        a=""
    if q==1:
        Y=Y+"7"
    a=a+"7"
    o.delete(0,10000)
    o.insert(0,a)
def f8():
    global a,Y,q
    if a=="Введите число":
        a=""
    if q==1:
        Y=Y+"8"
    a=a+"8"
    o.delete(0,10000)
    o.insert(0,a)
def f9():
    global a,Y,q
    if a=="Введите число":
        a=""
    if q==1:
        Y=Y+"9"
    a=a+"9"
    o.delete(0,10000)
    o.insert(0,a)
def f10():
    global a,Y,q
    if a=="Введите число":
        a=""
    if q==1:
        Y=Y+"0"
    a=a+"0"
    o.delete(0,10000)
    o.insert(0,a)
a0=tk.Button(text=0,width=8,height=3,bg="orange",fg="white",command=f10)
a1=tk.Button(text=1,width=8,height=3,bg="orange",fg="white",command=f1)
a2=tk.Button(text=2,width=8,height=3,bg="orange",fg="white",command=f2)
a3=tk.Button(text=3,width=8,height=3,bg="orange",fg="white",command=f3)
a4=tk.Button(text=4,width=8,height=3,bg="orange",fg="white",command=f4)
a5=tk.Button(text=5,width=8,height=3,bg="orange",fg="white",command=f5)
a6=tk.Button(text=6,width=8,height=3,bg="orange",fg="white",command=f6)
a7=tk.Button(text=7,width=8,height=3,bg="orange",fg="white",command=f7)
a8=tk.Button(text=8,width=8,height=3,bg="orange",fg="white",command=f8)
a9=tk.Button(text=9,width=8,height=3,bg="orange",fg="white",command=f9)
a0.place(x=67,y=134)
a1.place(x=0,y=20)
a2.place(x=67,y=20)
a3.place(x=134,y=20)
a4.place(x=201,y=20)
a5.place(x=0,y=77)
a6.place(x=67,y=77)
a7.place(x=134,y=77)
a8.place(x=201,y=77)
a9.place(x=0,y=134)
def n():
    global a,q,Y
    if a=="Введите число":
        a=""
    if a=="":
        a="0."
    elif a[-1]==".":
        a=a+""
    else:
        a=a+"."
    o.delete(0,10000)
    o.insert(0,a)
    if q==1:
        Y=Y+"."
n=tk.Button(text=".",width=8,height=3,bg="orange",fg="white",command=n)
n.place(x=134,y=134)
def h1():
    global a,q,D,X,f1,f2,f3,f4
    if a=="Введите число":
        a=""
    X=a
    D="+"
    f1="+"
    a=a+f1
    o.delete(0,10000)
    o.insert(0,a)
    q=1
def h2():
    global a,q,D,X,f1,f2,f3,f4
    if a=="Введите число":
        a=""
    X=a
    D="-"
    f2="-"
    a=a+f2
    o.delete(0,10000)
    o.insert(0,a)
    q=1
    f2=""
def h3():
    global a,q,D,X,f1,f2,f3,f4
    if a=="Введите число":
        a=""
    X=a
    D="*"
    f3="*"
    a=a+f3
    o.delete(0,10000)
    o.insert(0,a)
    q=1
    f3=""
def h4():
    global a,q,D,X,f1,f2,f3,f4
    if a=="Введите число":
        a=""
    X=a
    D="/"
    f4="/"
    a=a+f4
    o.delete(0,10000)
    o.insert(0,a)
    q=1
    f4=""
b1=tk.Button(text="+",width=8,height=3,bg="orange",fg="white",command=h1)
b2=tk.Button(text="-",width=8,height=3,bg="orange",fg="white",command=h2)
b3=tk.Button(text="*",width=8,height=3,bg="orange",fg="white",command=h3)
b4=tk.Button(text="/",width=8,height=3,bg="orange",fg="white",command=h4)
b1.place(x=0,y=191)
b2.place(x=67,y=191)
b3.place(x=134,y=191)
b4.place(x=201,y=191)
def r():
    global x,y,Y,X,D,T,l
    x=float(X)
    if l==1 and q==0:
        x=x*(-1)
    y=float(Y)
    if l==1 and q==1:
        y=y*(-1)
    if D=="+":
        T=x+y
    elif D=="-":
        T=x-y
    elif D=="*":
        T=x*y
    elif D=="/":
        T=x/y
    o.delete(0,10000)
    o.insert(0,T)
R=tk.Button(text="=",width=8,height=3,bg="orange",fg="white",command=r)
R.place(x=67,y=248)
def Z():
    global l,a
    l=1
    if a=="Введите число":
        a=""
    a=a+"-"
ZZ=tk.Button(text="--",width=8,height=3,bg="orange",fg="white",command=Z)
ZZ.place(x=201,y=134)
def ce():
    global a,x,y,T,Y,X,D,q,l
    x=y=T=q=l=0
    Y=X=D=""
    a=""
    o.delete(0,100000)
C=tk.Button(text="CE",width=8,height=3,bg="orange",fg="white",command=ce)
C.place(x=0,y=248)
w.mainloop()
