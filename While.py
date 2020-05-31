def func():
    a = int(input("Введите значение А: "))
    b = int(input("Введите значение Б: "))
    c = int(input("Введите значение В: "))

    while a <= b:
        a = a + c
        if a <= b:
            print("Значение А: ",  a, " - Пока что нет")
        elif a > b:
            print("Дождались! "  "Финальный А:", a)
func()

