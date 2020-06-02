num1 = int(input("Введите длину списка:"))
num2 = int(input("Ведите максимальное значение элемента списка: "))

def func_list(num1, num2):
    new_list = []
    for list1 in range(0, num1):
        new_list.append(randrange(0, num2))
print(new_list)

func_list(num1, num2)