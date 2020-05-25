a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if a > b:
    print("\nСвершилось!")
elif b > a:
    print("\nДа ну!")
elif a == b:
    print("\nА если так?")
    a = a + c
    b = b - c
    if a > b:
        print("\nСвершилось!")
    elif b > a:
        print("\nДа ну!")

