import json

with open("data_file.json", 'r') as json_file:                                                                  # Чтение заметок из json
    note_list = json.load(json_file)

def print_notes ():
    count = 1
    if len(note_list) == 0:                                                                                     # Проверка на пустой список
        print('Копировать код\nУ вас нет сохранённых заметок.')
    else:
        print('Список заметок:')
        for note_el in note_list:                                                                               # Вывод заметок
            print(f'\nЗаметка {count}')
            for j in note_el:
                print(f'{j}: {note_el[j]}')
            print('------------------------------------')
            count = count + 1

print_notes()