from random import randint

def func(k):
    file = open('G:\\Desktop\\Python\\homework4_py\\file.txt', 'w')
    #list = []
    a=int(0)
    for i in range(-k, -1):
        a=randint(0, 101)
        if a != 0:
            file.write (str(a))
            file.write ('*x^')
            file.write (str(-i))
            file.write ('+')
            #print (a, '*x^', -i ,'+', end='')
    a=randint(0, 101)
    if a != 0:
        file.write (str (a))
        file.write ('*x+')
    a=randint(0, 101)
    if a != 0:    
        file.write (str (a))
    file.write ('=0')
    
    
   
    
    file.close()

chislo = int(input ("Введите коэф k:"))

func(chislo)
   