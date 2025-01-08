import json

with open("data_file.json", 'r') as json_file:                                                      # Чтение заметок из json
    note_list = json.load(json_file)

def print_note ():
    count = 1
    print('Текукщий список заметок')
    for note_el_def in note_list:                                                                    # Функция вывода заметок
        print(f'\nЗаметка {count}')
        for key in note_el_def:
            print(f'{key}: {note_el_def[key]}')
        count = count + 1

print_note()

loop = True

while loop:                                                                                                             # Основной цикл
    del_index_list = []                                                                                                 # Список индексов для удаления заметок из списка
    del_index = input('Введите имя пользователя или заголовок для удаления заметки: ')
    search_ok = False                                                                                                   # Флаг нахождения заметки
    for note_el in note_list:                                                                                           # Цикл поиска
        if (note_el["Имя"].lower() == del_index.lower()) or (note_el["Заголовок"].lower() == del_index.lower()):        # Поиск совпадений по имени или заголовка, игнорируя регистр
            del_index_list.append(note_list.index(note_el))                                                             # Добавления индекса найденной заметки в список
            search_ok = True
            for i in del_index_list:
                yes_no = input(f'Вы действительно хотите удалить заметку {i+1}? (да/нет): ')
                if (yes_no == 'д') or (yes_no == 'да'):
                    del note_list[i]                                                                                    # Удаление заметок по индексу
                    print(f'Заметка {i+1} успешно удалена')
                elif (yes_no == 'н') or (yes_no == 'не') or (yes_no == 'нет'):
                    continue
    if search_ok:
        print_note()
        repit_no = input('Вы хотите повторить удаление? (да/нет): ')                                                    # Запрос на повторное удаление
        if (repit_no == 'д') or (repit_no == 'да'):
            continue
        elif (repit_no == 'н') or (repit_no == 'не') or (repit_no == 'нет'):
            loop = False
    else:
        research_no = input('Заметок с таким именем пользователя или заголовком не найдено. Хотите повторить посик? (да/нет): ')
        if (research_no == 'д') or (research_no == 'да'):                                                               # Запрос на повторный поиск, при отсуствии сопадений
            continue
        elif (research_no == 'н') or (research_no == 'не') or (research_no == 'нет'):
            loop = False

