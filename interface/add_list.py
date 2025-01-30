#Добавление нескольких заголовков

from add_input import username, content, status, created_date, issue_date
from utils.date_changer import date_changer_func

def add_title_list():
      title_list =[]

      title_list.append(input("Введите первый заголовок заметки: "))
      title_list.append(input("Введите второй заголовок заметки: "))
      title_list.append(input("Введите третий заголовок заметки: "))

      printable_titles = '; '.join(title_list)

      print(f"Имя пользователя: {username}\n"
            f"Заголовоки заметки: {printable_titles}\n"
            f"Основной текст заметки: {content}\nСтатус заметки: {status}\n"
            f"Дата создания заметки: {date_changer_func(created_date)}\n"
            f"Дата истечения заметки: {date_changer_func(issue_date)}")