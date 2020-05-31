def func():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

    while a <= b:
        a = a + c
        if a <= b:
            print("Значение А: ",  a, " - Пока что нет")
        elif a > b:
            print("Дождались! "  "Финальный А: ", a)
func()

