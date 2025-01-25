import json

from interface.display_notes import print_notes


def load_notes_from_file(filename):
    try:
        with open(f"{filename}.json", 'r') as json_file:  # Чтение заметок из json
            note_list = json.load(json_file)
        return note_list
    except FileNotFoundError:
        print('Такой файл не найден и был создан новый')
        with open(f"{filename}.json", 'w') as write_file:
            json.dump("", write_file, ensure_ascii=False)
    except json.JSONDecodeError as err:
        print(f"Ошибка декодирования JSON: {err}")

if __name__ == '__main__':
    notes = load_notes_from_file('data_file')

    print_notes(notes)