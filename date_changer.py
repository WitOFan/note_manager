#вывод даты в определённом формате

def date_changer_func (data):
      return data[0:5]

def print_test():
      print(date_changer_func('19.01.2038'))

if __name__ == '__main__':
    print_test()