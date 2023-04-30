import note_import, note_export

def note():
    print('Приложение заметки v.1.0')

    while True:
        print()
        print('Выберите действие:\n\
1 - создать заметку\n\
2 - сохранить заметку\n\
3 - читать список заметок\n\
4 - редактировать заметку\n\
5 - удалить заметку\n\
6 - выход\n')

        choice = input('Ваш выбор: ')
        print()
        match choice:
            case '1':
                print('Создание заметки:')
                note = note_import.note_making()

            case '2':
                print('Заметка сохранена')
                note_export.note_saving(note)

            case '3':
                print('Чтение:')
                note_import.note_reading()

            case '4':
                print('Редактирование заметки:')
                note_export.note_editing()

            case '5':
                print('Удаление заметки:')
                note_export.note_deleting()
            case '6':
                print('Досвидания')
                print()
                break

            case _:
                print('Вы выбрали недопустимое значение. Повторите выбор.')
