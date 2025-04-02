from string import ascii_letters

def first_word(text):
    word = ''
    allowed_chars = ascii_letters + "'"

    for i in text:
        if i in allowed_chars:
            word += i
        elif word:
            break

    return word

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

