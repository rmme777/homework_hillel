def popular_words(text, words):
    str_to_list = text.lower().split()
    count_dict = {}

    for i in words:
        count_dict[i] = 0

    for j in str_to_list:
        if j in count_dict:
            count_dict[j] += 1

    return count_dict


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')
