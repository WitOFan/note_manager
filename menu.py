from create_note_function import created_note
from display_notes import print_notes
from update_note_function import update_notes
from delete_note import del_note
from search_notes_function import search_note
import json

with open("data_file.json", 'r') as json_file:                                                                      # Чтение заметок из json
    note_list = json.load(json_file)

while True:
    print('Меню действий:\n'
          '1. Создать новую заметку\n'
          '2. Показать все заметки\n'
          '3. Обновить заметку\n'
          '4. Удалить заметку\n'
          '5. Найти заметки\n'
          '6. Выйти из программы')
    user_choice = input('Ваш выбор: ')
    if user_choice.isdigit():
        if 0 < int(user_choice) < 7:
            match int(user_choice):
                case 1:
                    note_list.append(created_note())
                case 2:
                    print_notes(note_list)
                case 3:
                    note_list = update_notes(note_list)
                case 4:
                    note_list = del_note(note_list)
                case 5:
                    search_note(note_list)
                case 6:
                    break
        else:
            print('Такого пункта меню не существует')
    else:
        print('Некорректный ввод. Введите число, соответствующее необходимому пункту меню')
