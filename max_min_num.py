import re


def min_max_numbers_search(text):
    my_list = []
    num = ''
    for i in range(0, len(text)):
        if re.search("[\-]", text[i]):
            if re.search("[\d]", text[i + 1]):
                num = num + str(re.search("[\-]", text[i]).group())
        if re.search("[\d]", text[i]):
            num = num + str(re.search("[\d]", text[i]).group())
            if i == len(text) - 1:
                my_list.append(num)
        else:
            if num != '' and num != '-':
                my_list.append(num)
                num = ''

    max_el = int(my_list[0])
    min_el = int(my_list[0])

    for j in range(1, len(my_list)):
        if int(my_list[j]) > max_el:
            max_el = int(my_list[j])
        if int(my_list[j]) < min_el:
            min_el = int(my_list[j])
    print('Min = ' + str(min_el) + ', Max = ' + str(max_el))


min_max_numbers_search('ks56kngwhg-1rthrh+2rhrh0rhr789h122rhr500rhr-678r')
