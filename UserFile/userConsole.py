import UserFile.Templater as m

def menu_console():
        m.printNenuTitle("Главное меню\n           Журнал заметок")
        print("1 - Показ журнала \n2 - Вывод заметки по id \n3 - Выбор заметки по дате\n4 - Редактирование заметки"
              " \n5 - Добавление заметки\n6 - Удаление заметки\n7 - Закончить программу")
        m.printMenuLine()
        print("\n Введите необходимый пункт ")