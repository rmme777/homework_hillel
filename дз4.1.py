list1 = [0, 1, 0, 12, 3]
list2 = [0]
list3 = [1, 0, 13, 0, 0, 0, 5]
list4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for_if = list1, list2, list3, list4


for row in for_if:
    copy_row = row.copy()
    for i in range(len(row) -1, -1, -1):
        if row[i] == 0:
            zero = row.pop(i)
            row.append(zero)
    print(f"{copy_row} => {row}")
