#сравнение с текущей датой

import datetime

current_dt = datetime.date.today()                                                                  # получение текущей даты
current_dt_str = current_dt.strftime('%d-%m-%Y')                                                    # и преобразование её в строку
print(f'Текущая дата: {current_dt_str}')

loop = True

issue_date = ''
issue_date_format = ''

while loop:                                                                                         # цикл на случай некорректного ввода
    issue_date = input('Введите дату дедлайна (в формате день-месяц-год): ')
    try:
        issue_date_format = datetime.datetime.strptime(issue_date, '%d-%m-%Y').date()        # преобразование строки в дату
        loop = False
    except ValueError:
        print('Пожалуйста, введите корректную дату')                                                # повтор при некорректном вводе
        continue

delta = issue_date_format - current_dt                                                              # нахождение разницы дат
delta_str = str(delta).split()[0]                                                                   # выделение дней из timedelta
if (int(delta_str[-1]) == 1) and (int(delta_str) != 11):                                            # определение день/дня/дней
    day = 'день'
elif (1 < int(delta_str[-1]) < 5) and ((10 > int(delta_str)) or int(delta_str) > 20):
    day = 'дня'
else:
    day = 'дней'
if issue_date_format > current_dt:                                                                   # если время до дедлайна ещё есть
    print(f'До дедлайна осталось {delta_str} {day}.')
else:                                                                                                # если времени уже нет
    print(f'Внимание! Дедлайн истёк {int(delta_str)*-1} {day} назад.')



