first_digit = int(input("Введите первое число: "))
enter_action = input("Введите действие:")
second_digit = int(input("Введите второе число: "))

match enter_action:
    case '+':
        print(first_digit + second_digit)
    case '-':
        print(first_digit - second_digit)
    case '*':
        print(first_digit * second_digit)
    case '/':
        print(first_digit / second_digit)
    case _:
        print("Неправильное действие")






