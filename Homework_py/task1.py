print ('Введите день недели цифрой от 1 до 7')
a=int(input())
if  a>=1 and a<=5:
    print ('это будний день')
elif a>5 and a<=7:
    print ('это выходной')
else: 
    print ('вы ввели некорректное число')

