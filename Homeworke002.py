import random

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = str(input("Введите вещественное число : "))
sum = 0
for i in number:
    if i != ".":
        sum += int(i)
print(sum)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input("Введите число : "))
a = 1
for i in range(1, num + 1):
    a *= i
    print(a, end=" ")
print()


# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму

n = int(input("Введите число : "))
sum = 0
for i in range (1, n + 1):
    a = (1 + 1 / i)**i 
    sum += a
    print(a, end=" ")
print(f"Сумма равна:  {sum}")   

# Реализуйте алгоритм перемешивания списка.

list = ["Anna", "Alex", 3.14159, 0]
for i in range(len(list)):
    index_a = random.randint(0, len(list) - 1)
    temp = list[i]
    list[i] = list[index_a]
    list[index_a] = temp
    
print(list)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

with open('file.txt', 'w') as data:
    data.write('0\n')
    data.write('1\n')
    data.write('2\n')
    data.write('3\n')
    data.write('4\n')
    data.write('5\n')
    data.write('6\n')

n = int(input("Введите кол-во элементов: "))

from random import randint
numbers = [randint(-n, n) for i in range(n)]
print(numbers)

data = open("file.txt", 'r')
dlist = [int(line.strip()) for line in data]
data.close()

mult = 1
for i in dlist:
    mult *= numbers[i]
print(mult)





