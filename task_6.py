# Дано число обозначающее день недели. 
# Вывести его название и указать является ли он выходным
list=['Monday', 'Tuesday', 'Wensday', 'Thursday', 'Friday','Saturday', 'Sunday']
day = int(input('enter a number from 1 to 7: '))
day-= 1

if day > 6 or day < 0:
    print('incorrect')
elif day ==5 or day == 6:
    print('Weekend', list[day])    
else:
    print('Weekday', list[day])
