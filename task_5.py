# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
number_a = float(input('введите число '))
print (f'кратно ли оно 5 и 10 или 15 но не 30: {(not number_a % 5 and not number_a % 10 or not number_a % 15) and (number_a % 30 != 0)} ')