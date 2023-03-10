import re


def alphabet_sorting(text):
    counter = 1
    my_list = list(text)
    while counter != 0:
        counter = 0
        for i in range(1, len(my_list) - 1):
            letter = my_list[i]
            if ord(letter) < ord(my_list[i - 1]):
                my_list[i] = my_list[i - 1]
                my_list[i - 1] = letter
                counter = counter + 1

    print(''.join(my_list))


alphabet_sorting('wasogpvmdkdjrjgmAkdkккккк')
