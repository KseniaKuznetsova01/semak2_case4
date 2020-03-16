import re
import string
lines_1 = []
with open('input.txt', 'r+') as input_file:
    text = input_file.read()
    for line in input_file.readlines():
        pr = text.find(' ')



with open('output.txt', 'w+') as output_file:

    for i in range(len(text)):
        if text[i] in string.ascii_letters or text[i] in string.digits or \
                text[i] in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ' or text[i] in '.,?!':
            output_file.writelines(text[i])

    print(text)
    line = input_file.readlines()

    for k in line:
        lines_1.append(list(filter(None, re.split('\W', k))))
    print()