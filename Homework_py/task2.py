from tkinter import Y


print ('Введите значение предикатов')
X=bool(input())
Y=bool(input())
Z=bool(input())

if  not(X or Y or Z) == (not X) or (not Y) or (not Z):
    print ('утверждение  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для этих предикат истинно')
else: 
    print ('утверждение  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для этих предикат не верно')