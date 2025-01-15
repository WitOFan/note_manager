import json

with open("data_file.json", 'r') as json_file:                                                                  # Чтение заметок из json
    note_list = json.load(json_file)

def print_notes (list_):
    count = 1
    if len(list_) == 0:                                                                                     # Проверка на пустой список
        print('Копировать код\nУ вас нет сохранённых заметок.')
    else:
        print('Список заметок:')
        for note_el in list_:                                                                               # Вывод заметок
            print(f'\nЗаметка {count}')
            for j in note_el:
                print(f'{j}: {note_el[j]}')
            print('------------------------------------')
            count = count + 1

if __name__ == '__main__':
    print_notes(note_list)