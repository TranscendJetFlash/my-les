__author__ = 'Кругов Д.О.'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a = []
    golden = 1.618034
    for i in range(n, m + 1):
        x = (golden ** i - (1 - golden) ** i) / (5 ** (1 / 2))
        a.append(round(x))
    return a

print(fibonacci(0, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(a):
    sorted_list = []
    for y in a:
        sorted_list.append(min(a))
        a.remove(min(a))
    return sorted_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_list(fucnt, param_b):
    end_list = list()
    for x in param_b:
        if fucnt(x) == True:
            end_list.append(x)
        else:
            continue
    return end_list


print((filter_list((lambda x: x > 5), param_b=[1, 100, 500, 7, 8, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

x1 = 1
x2 = 3
x3 = 5
x4 = 8
y1 = 2
y2 = 2
y3 = 6
y4 = 7

def parallelogram(x1,y1,x2,y2,x3,y3,x4,y4):
    if x4 - x1 == x3 - x2 and y2 == y3 and y1 == y4:
        parallelogram = 'yes'
    else:
        parallelogram = 'no'
    return parallelogram

print(parallelogram)