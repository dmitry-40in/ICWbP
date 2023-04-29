import datetime

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
                    list = data.readlines()
                    last_line = list[len(list) - 1].split(';')
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

        case '4':
            print('Вы выбрали 4')

        case '5':
            print('Вы выбрали 5')

        case '6':
            print('Досвидания.')
            break

        case _:
            print('Вы выбрали недопустимое значение. Повторите выбор.')




#             Приложение должно запускаться без ошибок, должно уметь сохранять данные
# в файл, уметь читать данные из файла, делать выборку по дате, выводить на
# экран выбранную запись, выводить на экран весь список записок, добавлять
# записку, редактировать ее и удалять