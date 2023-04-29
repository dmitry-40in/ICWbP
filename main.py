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
            date = "{}.{}.{}".format(dt.day, dt.month, dt.year)
            time = "{}:{}".format(dt.hour, dt.minute)

            note = id + ';' + header + ';' + body + ';' + date + ';' + time + '\n'

        case '2':
            print('Вы выбрали 2')
            with open('db.csv', 'a', encoding='utf8') as data:
                data.write(note)

        case '3':
            print('Вы выбрали 3')
            
            flag = True

            while flag:
                print('Выберите действие:\n1 - читать весь список заметок\n2 - применить фильтр по дате\n3 - выйти в основное меню\n')
                choice_filter = input('Ваш выбор: ')

                match choice_filter:
                    case '1':
                        with open('db.csv', 'r', encoding='utf8') as data:
                                print('ID / Header / Body / Date / Time')
                                for i in data.readlines():
                                    print(*i.split(';'), sep = '      ',end = '')
                    case '2':
                        # data_first = '30.04.2023'
                        print('Введите дату в формате день.мясяц.год. Пример: 31.01.2023\n')
                        data_first = input('Введите начала: ')
                        data_first_obj = datetime.strptime(data_first, '%d.%m.%Y')

                        # data_last = '1.05.2023'
                        data_last = input('Введите конца: ')
                        data_last_obj = datetime.strptime(data_last, '%d.%m.%Y')

                        with open('db.csv', 'r', encoding='utf8') as data:
                            print('ID / Header / Body / Date / Time')
                            for i in data.readlines():
                                line_list = i.split(';')
                                i_data_obj = datetime.strptime(line_list[3], '%d.%m.%Y')
                                if data_first_obj <= i_data_obj <= data_last_obj:
                                    print(*line_list, sep = '      ',end = '')




                    case '3':
                        flag = False
                    case _:
                        print('Вы выбрали недопустимое значение. Повторите выбор.')


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