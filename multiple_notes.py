import datetime

def created_note ():                                                                            # Функция добавления заметки
    note = {
        'Имя': input("\nВведите имя пользователя: "),
        'Заголовок': input('Введите заголовок заметки: '),
        'Описание': input("Введите основной текст заметки: "),
        'Статус': input("Введите статус заметки (новая, в процессе, выполнено): "),
        'Дата создания': input("Введите дату написания заметки в формате дд-мм-гггг: "),
        'Дедлайн': input("Введите дату завершения заметки (дедлайн) в формате дд-мм-гггг: ")
    }

    loop_in_def = True

    for el in note:                                                                              # Проверка на пустые строки
        if note[el] == '':
            print_el = el.lower()
            print(f'Вы отсавили значение "{print_el}" пустым, пожалуйста, введите {print_el}')
            note[el] = input(f'Введите {print_el}: ')
        else: continue

    while loop_in_def:                                                                          # Проверкка на корректную дату
        try:
            datetime.datetime.strptime(note['Дата создания'], '%d-%m-%Y').date()
            datetime.datetime.strptime(note['Дедлайн'], '%d-%m-%Y').date()
            loop_in_def = False
        except ValueError:
            print('Пожалуйста, введите корректную дату')
            note['Дата создания'] = input("Введите дату написания заметки в формате дд-мм-гггг: ")
            note['Дедлайн'] = input("Введите дату завершения заметки (дедлайн) в формате дд-мм-гггг: ")

    return note

loop = True

print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')

note_list = []

while loop:                                                                                     # Основной цикл добавления заметок
    note_list.append(created_note())
    yes_no = input('\nВотите добавить ещё одну заметку? (да/нет):')                             # функционал да/нет
    if (yes_no == 'д') or (yes_no == 'да'):                                                     # если да повтор ввода
        continue
    elif (yes_no == 'н') or (yes_no == 'не') or (yes_no == 'нет'):                              # если нет остановка цикла
        loop = False

count = 1

for note_el in note_list:                                                                        # Вывод заметки
    print(f'\nЗаметка {count}')
    for i in note_el:
        print(f'{i}: {note_el[i]}')
    count = count + 1