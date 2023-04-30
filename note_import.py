from datetime import datetime


def note_making():
    try:
        with open('db.csv', 'r', encoding='utf8') as data:
            i = data.readlines()
            if i != []:
                last_line = i[len(i) - 1].split(';')
                last_id = int(last_line[0])
                id = str(last_id + 1)
            else:
                id = '1'
    except FileNotFoundError:
        id = '1'

    header = input('Введите заголовок заметки:\n')
    body = input('Введите тело заметки:\n')

    dt = datetime.now()
    date = "{}.{}.{}".format(dt.day, dt.month, dt.year)
    time = "{}:{}".format(dt.hour, dt.minute)
    note = id + ';' + header + ';' + body + ';' + date + ';' + time + '\n'
    return note


def note_reading():
    flag = True

    while flag:
        print()
        print('Выберите действие:\n1 - читать весь список заметок\n2 - применить фильтр по дате\n3 - выйти в основное меню\n')
        choice_filter = input('Ваш выбор: ')

        match choice_filter:
            case '1':
                with open('db.csv', 'r', encoding='utf8') as data:
                    print()
                    print('ID / Header / Body / Date / Time')
                    for i in data.readlines():
                        print(*i.split(';'), sep='      ', end='')
                print()

            case '2':
                print('Введите дату в формате день.мясяц.год. Пример: 31.01.2023\n')
                data_first = input('Введите начальную дату: ')
                data_first_obj = datetime.strptime(
                data_first, '%d.%m.%Y')

                data_last = input('Введите конечную дату (может совпадать с начальной): ')
                data_last_obj = datetime.strptime(
                data_last, '%d.%m.%Y')

                with open('db.csv', 'r', encoding='utf8') as data:
                    print()
                    print('ID / Header / Body / Date / Time')
                    for i in data.readlines():
                        line_list = i.split(';')
                        i_data_obj = datetime.strptime(line_list[3], '%d.%m.%Y')
                        if data_first_obj <= i_data_obj <= data_last_obj:
                            print(*line_list, sep='      ', end='')
                print()

            case '3':
                flag = False

            case _:
                print('Вы выбрали недопустимое значение. Повторите выбор.')
