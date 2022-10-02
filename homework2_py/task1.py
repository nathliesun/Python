
def func(num):
    sum=0
    num = num.replace(',', '.')
    print(num)
    for symbol in num:
        if symbol != '.':
            sum +=int (symbol)
    return sum

if __name__ =="__main__":
    num1 = input ("Введите вещественное число:")
    sum1 = func(num1)
    print(sum1)