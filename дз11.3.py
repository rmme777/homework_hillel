def is_even(number):
    nums = '13579'
    n = str(number)
    if n[-1] in nums:
        return False
    else:
        return True


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
