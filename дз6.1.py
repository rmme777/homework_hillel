import string

ABC = string.ascii_letters


letters = input("Введите две английские буквы через дефис. Пример 'a-c': ")
first_letter = letters[0]
second_letter = letters[2]
first_letter_index = ABC.index(first_letter)
second_letter_index = ABC.index(second_letter)

if (len(letters) == 3) and (letters[0] in ABC) and (letters[2] in ABC) and (letters[1] == '-'):
    if first_letter_index < second_letter_index:
        print(ABC[first_letter_index:second_letter_index])
    elif first_letter_index > second_letter_index:
        print(ABC[first_letter_index:second_letter_index:-1])
else:
    print("Неверный ввод данных")



