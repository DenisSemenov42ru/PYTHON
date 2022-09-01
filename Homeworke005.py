# data = list(map(int, input("Введите числа: ").split()))
# print(data)
# data1 = [x for x in range(1,21)]
# print(data1)
# res = list(filter(lambda x: not x % 2, data1))
# print(res)


# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# def func_Del(string):
#     last_string = string.split(" ")

#     last_string1 = []
#     for i in last_string:
#         if i.find("абв") == -1:
#             last_string1.append(i)

#     string = " ".join(last_string1)

#     return string

# res_string = func_Del(" В этой абвварв строке должны абвтрина удалиться слова типрабв содержащие абв")
# print(res_string)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

# def coding(string):
#     count = 1
#     res = ''
#     for i in range(len(string)-1):
#         if string[i] == string[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + string[i]
#             count = 1
#     if count > 1 or (string[len(string)-2] != string[-1]):
#         res = res + str(count) + string[-1]
#     return res

# def decoding(string):
#     number = ''
#     res = ''
#     for i in range(len(string)):
#         if not string[i].isalpha():
#             number += string[i]
#         else:
#             res = res + string[i] * int(number)
#             number = ''
#     return res


# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")


# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

from pydoc import plain
from random import randint
import random

mode = int(input("Выберите режим игры: [1] - Два игрока, [2] - С ботом:  "))

def input_n(name):
        x = int(input(f"{name}, введите кол-во конфет которое возьмете от 1 до 28: "))
        while x < 1 or x > 28:
            x = int(input(f"{name}, введите корректное кол-во конфет: "))
        return x

def print_p(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, у него теперь {counter}. На столе осталось {value} конфет. ")

if mode == 1:

    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")
    value = int(input("Введите кол-во конфет на столе: "))
    flag = randint(0,2)
    if flag:
        print(f"Первым ходит {player1}")
    else:
        print(f"Первым ходит {player2}")

    counter1 = 0
    counter2 = 0

    while value > 28:
        if flag:
            k = input_n(player1)
            counter1 += k
            value -= k
            flag = False
            print_p(player1, k, counter1, value)
        else:
            k = input_n(player2)
            counter2 += k
            value -= k
            flag = True
            print_p(player2, k, counter1, value)

    if flag:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")


elif mode == 2:

    player1 = input("Введите имя  игрока: ")
    player2 = "Stupid_Bot"
    value = int(input("Введите кол-во конфет на столе: "))
    flag = randint(0,2)
    if flag:
        print(f"Первым ходит {player1}")
    else:
        print(f"Первым ходит {player2}")

    counter1 = 0
    counter2 = 0

    while value > 0:
        if flag:
            k = input_n(player1)
            counter1 += k
            value -= k
            flag = False
            print_p(player1, k, counter1, value)
        else:
            if value % 2 == 0:
                k = random.randrange(0, 28, 2)
            elif value <= 28:
                k = value
            else:
                k = random.randrange(0, 28, 1)

            counter2 += k
            value -= k
            flag = True
            print_p(player2, k, counter2, value)

    if flag:
        print(f"Выиграл {player2}")
    else:
        print(f"Выиграл {player1}")


# Создайте программу для игры в ""Крестики-нолики"".

print( " Крестики-нолики для двух игроков ")

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")