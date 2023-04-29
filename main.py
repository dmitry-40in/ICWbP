from datetime import datetime

print('Приложение заметки v.1.0')
print()

while True:
    print('Выберите действие:\n\
1 - создать заметку\n\
2 - сохранить заметку\n\
3 - читать список заметок\n\
4 - редактировать заметку\n\
5 - удалить заметку\n\
6 - выход')
    
    choice = input('Ваш выбор: ')

    match choice:
        case '1':
            print('Вы выбрали 1')
            try:
                with open('db.csv', 'r', encoding='utf8') as data:
                    i = data.readlines()
                    last_line = i[len(i) - 1].split(';')
                    last_id = int(last_line[0])
                    id = str(last_id + 1)
            except FileNotFoundError:
                id = '1'

            header = input('Введите заголовок заметки:\n')
            body = input('Введите тело заметки:\n')

            dt = datetime.now()
            date_time = "{}.{}.{} - {}:{}\n".format(dt.day, dt.month, dt.year, dt.hour, dt.minute) 

            note = id + ';' + header + ';' + body + ';' + date_time

        case '2':
            print('Вы выбрали 2')
            with open('db.csv', 'a', encoding='utf8') as data:
                data.write(note)

        case '3':
            print('Вы выбрали 3')
            with open('db.csv', 'r', encoding='utf8') as data:
                    print('ID / Header / Body / DateTime')
                    for i in data.readlines():
                        print(*i.split(';'), sep = '      ',end = '')

        case '4':
            print('Вы выбрали 4')
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
                                    note_edit[3] = "{}.{}.{} - {}:{}\n".format(dt.day, dt.month, dt.year, dt.hour, dt.minute)
                                    list_edit.append(';'.join(note_edit))
                                    flag = False
                                case _:
                                    print('Вы выбрали недопустимое значение. Повторите выбор.')

                    else:
                        
                        list_edit.append(i)
            with open('db.csv', 'w', encoding='utf8') as data:
                for i in list_edit:
                    data.write(i)

            

        case '5':
            print('Вы выбрали 5')
            list_edit = []
            note_edit = []
            note_number = input('Введите ID заметки для удаления: ')
            flag = True
            with open('db.csv', 'r', encoding='utf8') as data:
                for i in data.readlines():
                    line_i = i.split(';')
                    if note_number != line_i[0]:
                        list_edit.append(i)

            with open('db.csv', 'w', encoding='utf8') as data:
                for i in list_edit:
                    data.write(i)
            print(f'Заметка с ID = {note_number} удалена.')
        case '6':
            print('Досвидания.')
            break

        case _:
            print('Вы выбрали недопустимое значение. Повторите выбор.')




#             Приложение должно запускаться без ошибок, должно уметь сохранять данные
# в файл, уметь читать данные из файла, делать выборку по дате, выводить на
# экран выбранную запись, выводить на экран весь список записок, добавлять
# записку, редактировать ее и удалять