import os
from os import listdir
from os.path import isfile, join
import db
import warnings
import universal

warnings.filterwarnings("ignore")

def work_file():
    filename = input("Введите имя файла Egor-1point txt: ")
    f = open("%s" % filename, 'w+')
    count = 1
    while count <= 3:
        stri = input("Введите строку номер %s: " % count)
        f.write(stri + "\n")
        count+=1

    data = f.read()
    print(data)
    db.save_result("Содержимое файла Egor-1point", data)
    return f


def directoria():
    mypath = "C:/Users/aplyg/PycharmProjects/pract6"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(onlyfiles)
    db.save_result("Директория", onlyfiles)
    return


def renaiming():
    ren_file = input("Введите название переименнованного файла Egor-2points txt: ")
    os.rename('%s' % work_file(), '%s' % ren_file)
    db.save_result("Имя после переименования", ren_file)
    return


def create_catalog():
    path = r"C:\Users\aplyg\PycharmProjects\pract6\Kirill-3points"
    os.makedirs(path)  # мы используем функцию makedirs из модуля os, чтобы создать новую папку в указанном пути
    path1 = r"C:\Users\aplyg\PycharmProjects\pract6"
    directories = [f for f in os.listdir(path1) if os.path.isdir(os.path.join(path1, f))]
    db.save_result("Каталог", directories)

    print(directories)
    return


def redirector_file():
    path = r"C:\Users\aplyg\PycharmProjects\pract6\Kirill-3points"
    source_file = 'Egor-1point.txt'
    destination_folder = 'Kirill-3points'
    os.replace(source_file, os.path.join(destination_folder, os.path.basename(source_file)))
    full_file_path = os.path.join(path, 'Egor-1point.txt')
    print(full_file_path)
    db.save_result("Новый путь к файлу Egor-1point.txt", full_file_path)
    return


def size_file():
    file_name = 'Egor-2points.txt'
    file_size = os.path.getsize(file_name)
    print("Размер файла в байтах: %s" % file_size)
    db.save_result("Размер файла в байтах:", file_size)
    return


def main():
    run = True
    commands = """==========================================================================
1. Содержимое файла Egor-1point.txt, результат сохранить в MySQL.
2. Директория, результат сохранить в MySQL.
3. Имя после переименования, результат сохранить в MySQL.
4. Создать каталог, результат сохранить в MySQL.
5. Новый путь к файлу Egor-1point.txt, 
6. Размер файла в байтах Egor-2points.txt, 
7. Сохранить все данные из MySQL в Excel.
8. Завершить"""
    while run:
        run = universal.uni(commands,
                            db.check_db, work_file, directoria, renaiming,
                            create_catalog, redirector_file, size_file,
                            db.save_db_to_xlsx)
    return


if __name__ == '__main__':
    main()