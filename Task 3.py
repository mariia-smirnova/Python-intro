Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#Написать функцию, принимающую один позиционных аргумент N (целое число). Функция должна возвращать словарь где ключами будут индексы от 1 до N включительно, а значениями для этих ключей являются строки, образованные из случайных чисел диапазона [10, 99], преобразованных в строку по формату <первое число> <второе число>. В режиме дозаписи сохранять вывод функции в файле dict_park.txt

#ШАГ 1.Задаем кол-во строк от 1 до N
import random
from tkinter import N
n = int(input("Number of lines?"))
setn = list(range(1,n+1))
print(setn)

#ШАГ 2. Задаем кол-во объектов в строке
nn = int(input("Number of objects in line"))
setnn = list(range(1,nn+1))
print(setnn)

#ШАГ 3. Заполняем строки объектами
a = 0
for a in setnn:
     d = dict.fromkeys(range(1,nn+1), random.randint(10,99))
     print(d)
# к сожалению, не поняла, как сделать так, чтобы еще и в строчке значения были рандомные... тут даже цикл в цикле не получится, т.к значения должны быть в одном словаре (в строчку)

#ШАГ 4. Сохраняем в файл <.txt>
data = open('dict_park.txt', 'a')
data.write(d)
data.close()
