import datetime

date_str_1 = '30.4.2023'
date_str_2 = '2.4.2023'

date_obj_1 = datetime.datetime.strptime(date_str_1, '%d.%m.%Y')
date_obj_2 = datetime.datetime.strptime(date_str_2, '%d.%m.%Y')

if date_obj_2 > date_obj_1:
    print('yes')
else:
    print('no')