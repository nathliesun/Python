spisok=[1.1, 1.2, 3.1, 5, 10.01]
max=abs(spisok[0])%1
min=abs(spisok[0])%1

for i in range(1, len(spisok)):
    if isinstance (spisok[i], float):
        if max < abs(spisok[i]) %1:
            max = abs(spisok[i]) %1
        if min > abs(spisok[i]) %1:
            min = abs(spisok[i]) %1
    
d=round(max - min,2)
print(d)