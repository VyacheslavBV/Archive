def password():
    import random
    asmall='abcdefghijklmnopqrstuvwxyz'
    abig='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    anumb='123456789'
    n=int(input('Количество символов в пароле'))
    a1=list(asmall)
    a2=list(abig)
    a3=list(anumb)
    p=''
    for i in range(0,n):
        x=str(random.randint(1,3))
        if x=='1':
            q=random.randint(1,26)-1
            p=p+a1[q]
        elif x=='2':
            q = random.randint(1, 26)-1
            p = p + a2[q]
        elif x=='3':
            q = random.randint(1, 10)-2
            p = p + a3[q]
    print('Ваш пароль:', p)
password()

