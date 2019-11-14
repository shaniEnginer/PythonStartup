def fabo_cal(n):
    a=1
    b=1
    for i in range(n):
        yield a

        temp=a
        b=a
        b=temp+b

for i in fabo_cal(12):
    print(i)


