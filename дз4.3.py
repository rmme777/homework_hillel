import random

random_list = []
new_random_list = []

MIN_NUM = 1
MAX_NUM = 10

MIN_LEN = 3
MAX_LEN = 10

size = random.randint(MIN_LEN, MAX_LEN)
for _ in range(size):
    random_list.append(random.randint(MIN_NUM, MAX_NUM))

for _ in range(len(random_list)):
    new_random_list.append(random_list[0])
    new_random_list.append(random_list[2])
    new_random_list.append(random_list[-2])
    if len(new_random_list) == 3:
        break
print(f"{random_list} => {new_random_list}")
