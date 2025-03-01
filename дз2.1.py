# версия 1
numb = int(input("Введите 4х значное число: "))

print(n1 := numb // 1000)
print(n2 := numb % 1000 // 100)
print(n3 := numb % 100 // 10)
print(n4 := numb % 10)

# версия 2
for i in str(numb):
    print(i)