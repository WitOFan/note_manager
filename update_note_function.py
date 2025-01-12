import datetime
import json

with open("data_file.json", 'r') as json_file:                                                              # Чтение заметок из json
    note_list = json.load(json_file)

def update_note (dict_):
    while True:
        user_input = input('Выберите строку для редактирования (имя, статус, дедлайн и т.д.): ')
        search_ok = False                                                                                   # флаг посика ключа словаря
        no_flag = False                                                                                     # флаг отказа от редактирования выбранной строки
        for i in dict_:
            if user_input.lower() == 'Дедлайн'.lower():                                                     # если редактируют дедлайн
                yes_no = input(f'\nВотите действительно хотите изменить строку {i.lower()}? (да/нет):')     # функционал да/нет
                if (yes_no == 'д') or (yes_no == 'да'):                                                     # если да изменение значения
                    dict_[i] = input(f'Введите новое значение для строки {i.lower()} в формате дд-мм-гггг: ')

                    while True:                                                                             # Проверкка на корректную дату
                        try:
                            datetime.datetime.strptime(dict_[i], '%d-%m-%Y').date()
                            search_ok = True
                            print(f'Дата дедлайна заменена на {dict_[i]}')
                            break
                        except ValueError:
                            print('Пожалуйста, введите корректную дату')
                            dict_[i] = input("Введите дату завершения заметки (дедлайн) в формате дд-мм-гггг: ")

                elif (yes_no == 'н') or (yes_no == 'не') or (yes_no == 'нет'):                            # если нет повтор выбора строки
                    no_flag = True
                    continue

            elif user_input.lower() == i.lower():                                                           # все остальные подходящие ключи, кроме дедлайна
                yes_no = input(f'\nВотите действительно хотите изменить строку {i.lower()}? (да/нет):')     # функционал да/нет
                if (yes_no == 'д') or (yes_no == 'да'):                                                     # если да меняем значение
                    dict_[i] = input(f'Введите новое значение для строки {i.lower()}: ')
                    search_ok = True
                    while True:                                                                             # проверка на пустую стркоу
                        if dict_[i] == '':
                            print(f'Вы отсавили значение "{i.lower()}" пустым, пожалуйста, введите новое значение для {i.lower()}')
                            dict_[i] = input(f'Введите {i.lower()}: ')
                        else:
                            print(f'В строку {i.lower()} записано  {dict_[i]}')
                            break
                elif (yes_no == 'н') or (yes_no == 'не') or (yes_no == 'нет'):                              # если нет повтор выбора строки
                    no_flag = True
                    continue
            else: continue
        if search_ok: break                                                                                 # отсановка функции, если замена выполнена
        elif no_flag:                                                                                       # если сработал флаг отказа
            yes_no = input('\nХотите повторить ввод для редактирования заметок? (да/нет):')
            if (yes_no == 'д') or (yes_no == 'да'):
                continue
            elif (yes_no == 'н') or (yes_no == 'не') or (yes_no == 'нет'):
                break
        else:
            print('Вы ввели неверное значение, пожалуйста, повторите ввод')                                 # некорректный ввод
            continue

print('Текущий список заметок:')



def print_notes ():
    count = 1
    for note_el in note_list:                                                                               # Вывод заметок
        print(f'\nЗаметка {count}')
        for j in note_el:
            print(f'{j}: {note_el[j]}')
        count = count + 1

print_notes()

while True:                                                                                                 # Основной цикл
    note_number = input('\nВведите номер заметки, которую хотите отредактировать: ')
    if note_number.isdigit():                                                                               # Проверка на число
        if int(note_number) > len(note_list):                                                               # Проверка на существование заметки с таким номером
            print('Такой заметки не существует')
            continue
        else:
            update_note(note_list[int(note_number) - 1])
            print_notes()
            break
    else:
        print('Введите, пожалуйста, число, соответствующее номеру заметки')
        continue