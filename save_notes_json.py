import json

def save_notes_json(notes, filename):
    with open(f"{filename}.json", 'w') as write_file:
        json.dump(notes, write_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    with open("data_file.json", 'r') as json_file:  # Чтение заметок из json
        note_list = json.load(json_file)

    save_notes_json(note_list, "Notes")