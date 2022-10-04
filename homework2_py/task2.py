def func(N):
    spisok=[]
    x=1
    for i in range(1, N+1):
        x*=i
        spisok.append(x)
    print(spisok)



if __name__ =="__main__":
    N = int(input ("Введите число N:"))
    proizv = func(N)
   