import datetime

def created_note ():                                                                            # Функция добавления заметки
    note = {
        'Имя': input("\nВведите имя пользователя: "),
        'Заголовок': input('Введите заголовок заметки: '),
        'Описание': input("Введите основной текст заметки: "),
        'Статус': input("Введите статус заметки (новая, в процессе, выполнено): "),
        'Дедлайн': input("Введите дату завершения заметки (дедлайн) в формате дд-мм-гггг: ")
    }

    for el in note:                                                                             # Проверка на пустые строки
        if note[el] == '':
            print_el = el.lower()
            print(f'Вы отсавили значение "{print_el}" пустым, пожалуйста, введите {print_el}')
            note[el] = input(f'Введите {print_el}: ')
        else: continue

    while True:                                                                                 # Проверкка на корректную дату
        try:
            datetime.datetime.strptime(note['Дедлайн'], '%d-%m-%Y').date()
            break
        except ValueError:
            print('Пожалуйста, введите корректную дату')
            note['Дедлайн'] = input("Введите дату завершения заметки (дедлайн) в формате дд-мм-гггг: ")

    current_dt = datetime.date.today()                                                          # получение текущей даты
    current_dt_str = current_dt.strftime('%d-%m-%Y')
    note['Дата создания'] = current_dt_str

    return note

note_list = []

while True:
    yes_no = input('\nСоздать новую заметку? (да/нет):')                                        # функционал да/нет
    if (yes_no == 'д') or (yes_no == 'да'):                                                     # если да повтор ввода
        note_list.append(created_note())
    elif (yes_no == 'н') or (yes_no == 'не') or (yes_no == 'нет'):                              # если нет остановка цикла
        break

count = 1

for note_el in note_list:                                                                        # Вывод заметки
    print(f'\nЗаметка {count}')
    for i in note_el:
        print(f'{i}: {note_el[i]}')
    count = count + 1

