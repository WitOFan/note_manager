#Список для всего

note = []

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
    print(i)