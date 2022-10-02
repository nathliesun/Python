print ('Введите значение x, не равное нулю')
X=int(input())
print ('Введите значение y, не равное нулю')
Y=int(input())
if (X>0 and Y>0): 
    print ('1 четверть')
elif (X<0 and Y>0): 
    print ('2 четверть')
elif (X<0 and Y<0): 
    print ('3 четверть')
elif (X>0 and Y<0): 
    print ('4 четверть')
elif Y==0:
    print ('лежит на оси X')
elif X==0: 
    print ('лежит на оси Y')