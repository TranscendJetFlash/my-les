__author__ = 'Кругов Д.О.'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

# скрипт 1
for i in range(10):
    dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')


# срипт 2

for i in range(10):
    dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Такой директории не существует')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

dirs = os.listdir(path=os.getcwd())
print(dirs)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil

dir_to_copy = os.getcwd()
file_name = 'hw05_easy_copy_file.py'
shutil.copyfile(__file__, os.path.join(dir_to_copy, file_name))


def make_dir():
    import os
    dir_name = input("Введите название создаваемой директории: ")
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория успешно создана')
    except FileExistsError:
        print('Невозможно создать директорию - такая директория уже существует')

def delete_dir():
    import os
    dir_name = input("Какую директорию нужно удалить? ")
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('Директория успешно удалена')
    except FileNotFoundError:
        print('Невозможно удалить - такой директории не существует')

def list_files():
    from os import listdir, getcwd
    import os
    dirs = listdir(path=getcwd())
    print(dirs)

def change_dir():
    import os
    dir_name = input('В какую директорию перейти? ')
    try:
        path = os.path.join(os.getcwd(), dir_name)
        os.chdir(path)
        print('Вы успешно перешли в директорию'+ dir_name)
    except FileNotFoundError:
        print('Невозможно перейти - такой директории не существует')