import re


def numbers_search(text):
    result = []
    num = ''
    for i in range(0, len(text)):
        if re.search("[\d]", text[i]):
            num = num + str(re.search("[\d]", text[i]).group())
            if i == len(text) - 1:
                result.append(num)
        else:
            if num != '':
                result.append(num)
                num = ''
    print(result)


numbers_search('kdkdk1,tjtj100,300,rjrjrj5m25m32')
