def common_elements():
    first = set()
    second = set()
    for i in range(100):
        if i % 3 == 0:
            first.add(i)
        if i % 5 == 0:
            second.add(i)
    res = first.intersection(second)
    return res

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
