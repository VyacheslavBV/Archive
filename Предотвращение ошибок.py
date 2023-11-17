try :
    x=int(input())
except ValueError:
    print("Вот ты быдло")
    x=0
try :
    y=int(input())
except ValueError:
    print("Вот ты быдло")
    y=1
try:
    s=x/y
    print(s)
except ZeroDivisionError:
    print ("Нет,ну это уже просто блядство")
    S=0


    
