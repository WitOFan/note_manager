# Вводимые переменные

username = input("Введите имя пользователя: ")
content = input("Введите основной текст заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату написания заметки в формате дд.мм.гггг: ")
issue_date = input("Введите дату завершения заметки (дедлайн) в формате дд.мм.гггг: ")

#Функция для вывода принта и запроса заголовка только при исполнении этого файла напрямую
def print_test():
    title = input("Введите название заметки: ")
    print("Имя пользователя:", username, "\nЗаголовок заметки:", title,
            "\nОписание заметки:", content, "\nСтатус заметки:", status,
            "\nДата создания заметки:", created_date, "\nДата истечения заметки:", issue_date)

if __name__ == '__main__':
    print_test()
