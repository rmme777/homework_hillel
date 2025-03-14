import string

hashtag = input("Введите строку: ")
SPACE = " "
cleaned_hashtag = ""

for i in hashtag:
    if i not in string.punctuation:
        cleaned_hashtag += i

sentences = cleaned_hashtag.split(SPACE)
result = []
for i in sentences:
    result.append(i.capitalize())
corrected_sentence = "".join(result)
sentence_140len = []
if len(corrected_sentence) > 140:
    for j in range(140):
        for k in corrected_sentence[j]:
            sentence_140len.append(k)
    corrected_sentence_140len = "".join(sentence_140len)
    print(f"#{corrected_sentence_140len}")
else:
    print(f"#{corrected_sentence}")