import datetime
import json

def data_check (data):
    while True:  # Проверкка на корректную дату
        try:
            datetime.datetime.strptime(data, '%d-%m-%Y').date()
            search_ok = True
            print(f'Дата дедлайна заменена на {data}')
            break
        except ValueError:
            print('Пожалуйста, введите корректную дату')
            data = input("Введите дату завершения заметки (дедлайн) в формате дд-мм-гггг: ")
    return search_ok

def check_empty_string (string, name_string):
    while True:                                                                                             # проверка на пустую стркоу
        if string == '':
            print(
                f'Вы отсавили значение "{name_string.lower()}" пустым, пожалуйста, введите новое значение для строки {name_string.lower()}')
            string = input(f'Введите {name_string.lower()}: ')
        else:
            print(f'В строку {name_string.lower()} записано  {string}')
            break

def update_note (note):
    while True:
        user_input = input('Выберите строку для редактирования (имя, статус, дедлайн и т.д.): ')
        search_ok = False                                                                                   # флаг посика ключа словаря
        no_flag = False                                                                                     # флаг отказа от редактирования выбранной строки
        for field in note:
            if user_input.lower() == 'Дедлайн'.lower():                                                     # если редактируют дедлайн
                yes_no = input(f'\nВотите действительно хотите изменить строку {field.lower()}? (да/нет):')     # функционал да/нет
                if (yes_no == 'д') or (yes_no == 'да'):                                                     # если да изменение значения
                    note[field] = input(f'Введите новое значение для строки {field.lower()} в формате дд-мм-гггг: ')
                    search_ok = data_check(note[field])

                elif (yes_no == 'н') or (yes_no == 'не') or (yes_no == 'нет'):                              # если нет повтор выбора строки
                    no_flag = True
                    continue

            elif user_input.lower() == field.lower():                                                       # все остальные подходящие ключи, кроме дедлайна
                yes_no = input(f'\nВотите действительно хотите изменить строку {field.lower()}? (да/нет):') # функционал да/нет
                if (yes_no == 'д') or (yes_no == 'да'):                                                     # если да меняем значение
                    note[field] = input(f'Введите новое значение для строки {field.lower()}: ')
                    search_ok = True
                    check_empty_string(note[field], field)
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

def update_notes (list_):
    while True:                                                                                                 # Основной цикл
        note_number = input('\nВведите номер заметки, которую хотите отредактировать: ')
        if note_number.isdigit():                                                                               # Проверка на число
            if int(note_number) > len(list_):                                                               # Проверка на существование заметки с таким номером
                print('Такой заметки не существует')
                continue
            else:
                update_note(list_[int(note_number) - 1])
                #print_notes()
                break
        else:
            print('Введите, пожалуйста, число, соответствующее номеру заметки')
            continue
    return list_


if __name__ == '__main__':
    with open("data_file.json", 'r') as json_file:  # Чтение заметок из json
        note_list = json.load(json_file)

    print('Текущий список заметок:')
    def print_notes ():
        count = 1
        for note_el in note_list:                                                                               # Вывод заметок
            print(f'\nЗаметка {count}')
            for field in note_el:
                print(f'{field}: {note_el[field]}')
            count = count + 1

    print_notes()
    update_notes(note_list)
    print_notes()