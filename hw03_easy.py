__author__ = 'Кругов Д.О.'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


#вариант 1
def my_round(number, ndigits):
    pass

def my_round(number, ndigits):
    number = number*(10**ndigits)+0.41
    number = number//1
    return number/(10**ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
import math
def lucky_ticket(ticket_number):
    x = list(str(ticket_number))
    a = x[:3]
    a = list(map(int, a))
    b = x[3:]
    b = list(map(int, b))
    sum_1 = 0
    sum_2 = 0
    for sum1 in a:
        sum_1 = sum1 + sum_1
    for sum2 in a:
        sum_2 = sum2 + sum_2
    if sum_1 == sum_2:
        ticket_number = 'yes'
    else:
        ticket_number = 'no'
    return ticket_number

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))