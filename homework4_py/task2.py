def mnog(n):                                
    list = []
    for i in range(2, int(n / 2) + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:                                           # найдя множитель, делим его до простого
            if n % i == 0:
                n = n / i
                list.append(i)
                print('Множитель', n )
    return list

def main():
    num = int(input('Ведите натуральное число '))
    list = mnog(num)
    if len(list) > 0:
        print('Простые множители:') 
        print(list)
    else:
        print('Нет простых множителей') 

main()