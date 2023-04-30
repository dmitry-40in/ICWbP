from datetime import datetime


def note_saving(note):
    with open('db.csv', 'a', encoding='utf8') as data:
                    data.write(note)


def note_editing():
    list_edit = []
    note_edit = []
    note_number = input('Введите ID заметки для редактирования: ')
    flag = True

    with open('db.csv', 'r', encoding='utf8') as data:
        for i in data.readlines():
            line_i = i.split(';')
            if note_number == line_i[0]:
                note_edit = line_i.copy()
                print(f'Редактируем заметку ID = {note_number}')
                while flag:
                    choice_edit = input('Выберите действие:\n1 - изменить заголовок заметки\n2 - изменить тело заметки\n3 - сохранить и выйти в основное меню\n')
                    match choice_edit:
                        case '1':
                            note_edit[1] = input('Введите новый заголовок: ')
                        case '2':
                            note_edit[2] = input('Введите новое тело заметки: ')
                        case '3':
                            dt = datetime.now()
                            note_edit[3] = "{}.{}.{}".format(dt.day, dt.month, dt.year)
                            note_edit[4] = "{}:{}\n".format(dt.hour, dt.minute)
                            list_edit.append(';'.join(note_edit))
                            flag = False
                        case _:
                            print('Вы выбрали недопустимое значение. Повторите выбор.')

            else:
                list_edit.append(i)

            with open('db.csv', 'w', encoding='utf8') as data:
                for i in list_edit:
                    data.write(i)


def note_deleting():
    list_edit = []
    note_number = input('Введите ID заметки для удаления: ')

    with open('db.csv', 'r', encoding='utf8') as data:
        for i in data.readlines():
            line_i = i.split(';')
            if note_number != line_i[0]:
                list_edit.append(i)

    with open('db.csv', 'w', encoding='utf8') as data:
        for i in list_edit:
            data.write(i)
    print(f'Заметка с ID: {note_number} удалена')
