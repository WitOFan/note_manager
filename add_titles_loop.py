# циклическое добавление заметок

title_list =[] # список с заметакми

loop = True # флаг остановки цикла

while loop:                                                                             # основной цикл
    title_temp = input("Введите заголовок (или оставьте пустым для завершения): ")      # ввод заголовка
    if not title_temp:                                                                  # проверка на пустую строку
        loop = False                                                                    # если строка пуста цикл остановится
        if len(title_list) == 0:                                                        # если в списке нет ни одного заголовка
            print('Вы не ввели ни одного заголовка')                                    # программа об этом сообщит
        else:                                                                           # если список не пуст
            print('\nЗаголовки заметки:')                                               # выведуться введённые заголовки
            for i in title_list:
                print(f'- {i}')
    else:                                                                               # если строка не пуста цикл повториться
        title_list.append(title_temp)