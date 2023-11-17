n=0
l=0
o=''
for i in range(12,1000):
    for j in range(1,i):
        l=0
        if j**2==i or j**3==i:
            break
        else:
            l=1
    if l==1:
        o=o+str(i)
        n = n + len(str(i))
    if n>2022:
        break
o=list(o)
print(o[2021])

