def create_list():
    x = int(input("Введите длину списка: "))
    y = int(input("Введите максимально возможное значение элемента списка: "))

    list1 = [random.randint(1, y) for i in range(x)]

    return list1

# вызов функции
print(create_list())