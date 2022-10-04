def func(N):
    spisok=[]
    x=1
    sum=float(0)
    for i in range(1, N+1):
        x=round(((1+1/i)**i),3)
        spisok.append(x)
    print(spisok)
    for i in range(0, len(spisok)):
        sum+=spisok[i]    
    print(sum)


if __name__ =="__main__":
    N = int(input ("Введите число N:"))
    sum = func(N)
   


