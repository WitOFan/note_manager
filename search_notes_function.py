import json

def search_core(notes, keyword=None, status=None):
    search_list = []

    for note_el in notes:                                                                                           # Цикл поиска
        if (type(keyword) == str) and (type(status) == str):                                                        # Поиск по ключевому слову и статусу
            if note_el["Статус"].lower() == status.lower():
                for i in note_el:
                    if keyword.lower() in note_el[i].lower():
                        search_list.append(note_el)
                        break
        elif type(keyword) == str:                                                                                  # Поиск по ключевому слову
            for field in note_el:
                if keyword.lower() in note_el[field].lower():
                    search_list.append(note_el)
                    break
        elif type(status) == str:                                                                                   # Поиск по статусу
            if note_el["Статус"].lower() == status.lower():
                search_list.append(note_el)

    if len(search_list) == 0:                                                                                       # Если ничего не найдено
        print('Подходящих заметок не найдено')
    else:                                                                                                           # Если поиск успешный
        count = 1
        print('Найденные заметки:')
        for search_el in search_list:  # Вывод заметок
            print(f'\nЗаметка {count}')
            for field in search_el:
                print(f'{field}: {search_el[field]}')
            print('------------------------------------')
            count = count + 1

def search_note (notes):
    while True:
        print('Выбирете способ посика:\n'
              '1. Поиск по ключевому слову\n'
              '2. Поиск по статусу\n'
              '3. Поиск по ключевому слову и статусу\n')
        user_choice = input('Введите число: ')
        if user_choice == '1':                                                                                          # Поиск по ключевому слову
            user_keyword = input('Введите ключевое слово для поиска: ')
            search_core(notes, user_keyword.strip())
        elif user_choice == '2':                                                                                        # Поиск по статусу
            user_status = input('Введите статус заметки для поиска: ')
            search_core(notes, status=user_status.strip())
        elif user_choice == '3':                                                                                        # Поиск по ключевому слову и статусу
            user_keyword = input('Введите ключевое слово для поиска: ')
            user_status = input('Введите статус заметки для поиска: ')
            search_core(notes, user_keyword.strip(), user_status.strip())
        else:                                                                                                           # Некорректный ввод
            print('Пожалуйста, введите число, обозначающее вариант поиска (1, 2, 3)')
            continue
        repeat_no = input('Вы хотите повторить поиск? (да/нет): ')                                                      # Запрос на повторный поиск
        if (repeat_no == 'д') or (repeat_no == 'да'):
            continue
        elif (repeat_no == 'н') or (repeat_no == 'не') or (repeat_no == 'нет'):
            break

if __name__ == '__main__':
    with open("data_file.json", 'r') as json_file:  # Чтение заметок из json
        note_list = json.load(json_file)

    search_note(note_list)