# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = input("Введите числа через пробел : ").split()
sum = 0
for i in range(len(lst)):
   if i % 2 != 0:
       sum += int(lst[i])
print(sum)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д

lst = input("Введите числа через пробел : ").split()
product = []
for i in range((len(lst) + 1)//2):
    product.append(int(lst[i]) * int(lst[len(lst)-1-i]))
print(product)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = list(map(float, input("Введите числа через пробел: ").split()))
max = 0
min = 1
for i in lst:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)
print(round(max - min, 2))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное

number = int(input("Введите число: "))
num = ""
while number > 0:
    num += str(number % 2) 
    number = number // 2
print(f"Ваше число в двоичном представлении: {num}")

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

num = int(input('Введите число: '))
nums = []
n1, n2 = 1, 1
for i in range(num):
        nums.append(n1)
        n1, n2 = n2, n1 + n2
n1, n2 = 0, -1
for i in range (num + 1):
    nums.insert(0, n1)
    n1, n2 = n2, n1 + n2
print(nums)
