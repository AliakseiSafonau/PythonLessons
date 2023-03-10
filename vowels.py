import re


def vowel_count(text):
    result = 0
    for i in range(0, len(text) - 1):
        if re.search("[AEIOUYaeiouy]", text[i]):
            result = result + 1
    print(result)


vowel_count(input('Введите текст : '))
