n = int(input('Введите число '))
def fibonacci(n):
    nums = []
    a, b = 1, 1
    for i in range(n):
        nums.append(a)
        a, b = b, a + b
    a, b = 0, 1 
    for i in range(0, n+1):
        nums.insert(0, a)
        a, b = b, a - b
    return nums

nums= fibonacci(n)
print(fibonacci(n))



