import string
def is_palindrome(text):
    clear_str = ""
    for i in text:
         if i in string.punctuation:
             continue
         else:
            clear_str += i
    last_dig = -1
    for j in clear_str.lower().replace(" ", ""):
         if j == clear_str.lower().replace(" ", "")[last_dig]:
            last_dig -=1
         else:
             return False
    return True




assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
