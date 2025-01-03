#Список, как было сказано в задании 5

'''note = []

note.append(input("Введите имя пользователя: "))
note.append(input("Введите основной текст заметки: "))
note.append(input("Введите статус заметки: "))
note.append(input("Введите дату написания заметки в формате дд.мм.гггг: "))
note.append(input("Введите дату завершения заметки (дедлайн) в формате дд.мм.гггг: "))

title_list =[]

title_list.append(input("Введите первый заголовок заметки: "))
title_list.append(input("Введите второй заголовок заметки: "))
title_list.append(input("Введите третий заголовок заметки: "))

note.append(title_list)

for i in note:
    print(i)'''

#Словарь, как сказано в завершении этапа

note = {
    'username': input("Введите имя пользователя: "),
    'content': input("Введите основной текст заметки: "),
    'status': input("Введите статус заметки: "),
    'created_date': input("Введите дату написания заметки в формате дд.мм.гггг: "),
    'issue_date': input("Введите дату завершения заметки (дедлайн) в формате дд.мм.гггг: ")
}

title_list =[]

title_list.append(input("Введите первый заголовок заметки: "))
title_list.append(input("Введите второй заголовок заметки: "))
title_list.append(input("Введите третий заголовок заметки: "))

note ['titles'] = title_list

for i in note:
    print(f'{i}: {note[i]}')

