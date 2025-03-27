def difference(*args):
    args_list = []
    if not args:
        return 0

    elif args == int or float:
        for i in args:
            args_list.append(i)

        biggest_num = max(args_list)
        smallest_num = min(args_list)
        return round(biggest_num - smallest_num, 2)

    else:
        print('Неверный ввод данных')
        exit()


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
