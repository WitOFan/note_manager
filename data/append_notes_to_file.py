import os

def append_notes_to_file(notes, filename):
    with open(f"{filename}.txt", 'a', encoding='utf-8') as file_read:
        if os.stat(f"{filename}.txt").st_size > 0:
            notes_str = str(notes).replace('[', ', ')
            notes_str = notes_str.replace(']', '')
            file_read.write(notes_str)
        else:
            notes_str = str(notes).replace(']', '')
            notes_str = notes_str.replace('[', '')
            file_read.write(notes_str)
if __name__ == '__main__':
    notes = [
        {
            "Имя": "Андрей",
            "Заголовок": "Первый",
            "Описание": "основной текст заметки",
            "Статус": "Новая",
            "Дата создания": "08-01-2025",
            "Дедлайн": "10-01-2025"
        },
        {
            "Имя": "Данил",
            "Заголовок": "Второй",
            "Описание": "основной текст заметки",
            "Статус": "В процессе",
            "Дата создания": "08-01-2025",
            "Дедлайн": "10-01-2025"
        }]

    append_notes_to_file(notes, 'Notes')