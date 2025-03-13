while True:
    first_digit = int(input("Введите первое число: "))
    enter_action = input("Введите действие (+, -, *, /): ")
    second_digit = int(input("Введите второе число: "))

    match enter_action:
        case '+':
            print(first_digit + second_digit)
        case '-':
            print(first_digit - second_digit)
        case '*':
            print(first_digit * second_digit)
        case '/':
            if second_digit == 0:
                print("Ошибка: деление на ноль!")
            else:
                print(first_digit / second_digit)
        case _:
            print("Неправильное действие")

    while True:
        cont = input("Do you want to continue? (Y/N): ").strip().upper()
        if cont == 'N':
            exit()
        elif cont == 'Y':
            break
        else:
            print("Incorrect command, please enter 'Y' or 'N'.")
