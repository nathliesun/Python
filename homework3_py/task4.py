print("Введите целое число")
dec= int (input())
def convert(dec):
    bin = ' '
    if dec > 0:
        while dec !=0:
            bin= str(dec % 2) + bin
            dec //= 2
        print(f'Двоичное число: {bin}.')
    else: 
        print ('Вы ввели не целое число')
convert (dec)