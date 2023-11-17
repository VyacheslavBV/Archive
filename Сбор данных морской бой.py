
def d():
    A = [''] * 12
    B = [''] * 12
    C=[''] * 12
    D=[''] * 12
    E=[''] * 12
    F=[''] * 12
    G=[''] * 12
    H=[''] * 12
    I=[''] * 12
    K=[''] * 12
    J=[''] * 12
    L=[''] * 12
    BigMass = [A, B, C, D, E, F, G, H, I, J, K, L]
    d=str(input('Введите первый участок'))
    md=list(d)
    a=md[0]
    try:
        if md[2]!='':
            try:
                b=int(str(md[1])+str(md[2]))
            except (ValueError):
                print('Неправильный формат данных')
                exit()
    except(IndexError):
        try:
            b=int(md[1])
        except (ValueError):
            print('Неправильный формат данных')
            exit()
    if a>'l':
        print('Неправильный формат данных')
        exit()
    elif b>12:
        print('Неправильный формат данных')
        exit()
    b=b-1
    if a=='a' or a=='A':
        A[b]='x'
    elif a=='b' or a=='B':
        B[b]='x'
    elif a=='c' or a=='C':
        C[b]='x'
    elif a=='D' or a=='d':
        D[b]='x'
    elif a=='e' or a=='E':
        E[b]='x'
    elif a=='F' or a=='f':
        F[b]='x'
    elif a=='g' or a=='G':
        G[b]='x'
    elif a=='H' or a=='h':
        H[b]='x'
    elif a=='i' or a=='I':
        I[b]='x'
    elif a=='j' or a=='J':
        J[b]='x'
    elif a=='K' or a=='k':
        K[b]='x'
    elif a=='l' or a=='L':
        L[b]='x'
    else:
        print('Вне области буквенных значений')
    for i in range(0,12):
        print(BigMass[i])
d()

