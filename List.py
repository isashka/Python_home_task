def create_list():
    x = int(input('Введите длину списка: '))
    y = int(input('Введите максимально возможное значение элемента списка: '))

    lst = [random.randint(1, y) for i in range(x)]

    return lst

# вызов функции
print(create_list())