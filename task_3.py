# Вывести на экран числа от -N до N
number_n = int(input('введите число N '))
for i in range(-number_n, number_n + 1):
    print(i, end = ' , ')