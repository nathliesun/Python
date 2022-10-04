spisok=[1, 2, 3, 4, 5, 6, 7,8,9,10,11,12]
proizv = 0

print('длина массива равна' , len(spisok) )

while len(spisok) >1:
    proizv = spisok[0] * spisok[(len(spisok)-1)] 
    print (proizv)
    spisok.pop(0) 
    spisok.pop(len(spisok)-1)
if len(spisok) == 1:   
    proizv = spisok[0]*spisok[0]
    print (proizv)
    



