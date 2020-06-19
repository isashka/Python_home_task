text_str = input("Напишите любое предложение: ")
letter_str = input("Какую букву Вы хотите посчитать в нем?: ")

sym = text_str.count(letter_str)

print("В строке", text_str, "символ", letter_str, "встречается", sym, "раз/а")
