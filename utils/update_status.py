#обновление статуса заметки на основе введённых пользователем данных


status_list = ['Памятка', 'Важная', 'Не срочная']   # в перспективе список можно заменить на .json файл, чтобы сохранять
                                          # введённые статусы
def update_status(status_list):
    print ('Список сохранённых статусов:\n')
    count = 1
    for i in status_list:
        print(f'{count}. {i}')
        count = count + 1

    while True:                                                                                             # цикл для повторного ввода в случае ошибки
        user_choice = input('\nВыберете статус из имеющихся или добавте свой: ')
        if user_choice.isdigit():                                                                           # проверка на ввод числа
            if int(user_choice) > len(status_list):                                                         # проверка на ввод корректного числа
                yes_no = input('\nВы ввели число больше, чем количество сохранённых заметок, хотите ли вы установить его как статус?'
                      '\ny - установить число как статус, n - повторить ввод\n')                            # функционал да/нет
                if (yes_no == 'y') or (yes_no == 'ye') or (yes_no == 'yes'):                                # если да число становится новым статусом
                    status_list.append(user_choice)
                    print(f'\nВы изменили статус на: {user_choice}')
                    break
                elif (yes_no == 'n') or (yes_no == 'no') or (yes_no == 'not'):                              # если нет повтор цикла
                    continue
                else:                                                                                       # обработка некорректного ввода
                    print('\nВведено некорректное значение, пожалуйста, следуйте рекомендациям')
                    continue
            else:                                                                                           # выбор статуса из списка
                print(f'\nВы изменили статус на: {status_list[int(user_choice) - 1]}')
                break
        else:                                                                                               # ввод нового статуса
            status_list.append(user_choice)
            print(f'\nВы изменили статус на: {user_choice}')
            break


if __name__ == '__main__':
    update_status(status_list)