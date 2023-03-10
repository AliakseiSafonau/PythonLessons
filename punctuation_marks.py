import re


def remove_punctuation_marks(text):
    result = re.sub("\W", '', text)
    print(result)


remove_punctuation_marks('kgjgj,glt,,,ktt,,,ir,.!!@kk2kf...fk.,,;fkfkf;fkf,')
