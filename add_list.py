#Добавление нескольких заголовков

from add_input import *
from date_changer import date_changer_func

title_1 = input("Введите первый заголовок заметки: ")
title_2 = input("Введите второй заголовок заметки: ")
title_3 = input("Введите третий заголовок заметки: ")

title_list = [title_1, title_2, title_3]
printable_titles = '; '.join(title_list)

print(f"Имя пользователя: {username}\n"
      f"Заголовоки заметки: {printable_titles}\n"
      f"Основной текст заметки: {content}\nСтатус заметки: {status}\n"
      f"Дата создания заметки: {date_changer_func(created_date)}\n"
      f"Дата истечения заметки: {date_changer_func(issue_date)}")