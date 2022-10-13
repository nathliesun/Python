import math

def func(n):
    p=float(0)
    i=int(0)
    while((math.pi-p)>n):
        p+=8/((4*i+1)*(4*i+3))
        i+=1
    return p

p=func(0.001)
print('Число Пи равно ', p, ' с точностью ', math.pi-p)
