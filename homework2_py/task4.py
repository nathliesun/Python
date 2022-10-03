from random import randint

def func(N):
    lst=[]
    mult=1
    for i in range(N):
        lst.append(randint(-N, N))
    print(lst)
    print(len(lst))
    file = open('G:\\Desktop\\Python\\homework2_py\\file.txt', 'r')
    for line in file:
        if int(line) < len(lst):
            mult*=lst[int(line)]
    file.close()
    print(mult)



 
if __name__ =="__main__":
    chislo = int(input ("Введите число N:"))
    func(chislo)
