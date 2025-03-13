import keyword
import string

name_string = input("Введите строку: ")
NUMS = "0123456789"

if not name_string:
    print(False)

else:
    for i in name_string:
        if i in string.ascii_uppercase:
            print(False)
            break
    else:
        if name_string[0] in NUMS:
            print(False)

        else:
            for char in name_string:
                if char in string.punctuation and char != "_":
                    print(False)
                    break
            else:
                if name_string.count("_") > 1:
                    print(False)

                elif name_string in keyword.kwlist:
                    print(False)

                else:
                    print(True)
