class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

number_list = []
while True:
    try:
        value = input('Введите целое число в список:')
        if value == 'stop':
            print(number_list)
            break
        if not value.isdigit():
            raise MyOwnError("Ошибка.Это не целое число")
        else:
            number_list.append(int(value))
    except MyOwnError as err:
        print(err)

