while True:
    print('Выберите действие:\n1 - создать заметку\n2 - сохранить заметку\n3 - читать список заметок\n\
4 - редактировать заметку\n5 - удалить заметку\n6 - выход')
    choice = input('Ваш выбор: ')

    match choice:
        case '1':
            print('Вы выбрали 1')
        case '2':
            print('Вы выбрали 2')
        case '3':
            print('Вы выбрали 3')
        case '4':
            print('Вы выбрали 4')
        case '5':
            print('Вы выбрали 5')
        case '6':
            print('Вы выбрали 6')
        case _:
            print('Вы выбрали недопустимое значение. Повторите выбора.')