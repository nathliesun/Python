spisok=[1, 2, 3, 4, 5, 6, 7]
sum = 0
print('длина массива равна' , len(spisok))
for i in range(0, len(spisok)):
    if ((i+1) % 2) != 0: 
        print (spisok[i])
        sum = sum + spisok[i]
    
print('сумма чисел на нечетных позициях равна', sum)
