secundas = int(input("Введите кол-во секунд от 0 до 8640000: "))

days = 0
hours = 0
minutes = 0
secs = 0

if 0 <= secundas < 8640000:
    days = str(secundas // 86400)
    hours = secundas % 86400 // 3600
    minutes = secundas % 86400 % 3600 // 60
    secs = secundas % 60

    if hours < 10:
        hours = '0' + str(hours)

    if minutes < 10:
        minutes = '0' + str(minutes)

    if secs < 10:
        secs = '0' + str(secs)

    if (days == '1') or (days[-1] == '1'):
        print(f"{days} день, {hours}:{minutes}:{secs}")
    elif (days == '2' or '3' or '4') or (days[-1] == '2' or '3' or '4'):
        print(f"{days} днi, {hours}:{minutes}:{secs}")
    else:
        print(f"{days} днiв, {hours}:{minutes}:{secs}")
else:
    print("Неверный ввод данных.")

