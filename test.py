import string
import re
spisok = []
lines_1 = []
lines_2 = []
with open('input.txt', 'r+') as file:
    lines = file.readlines()
    print(lines)
    for j in lines:
        line = j[:-1]
        spisok.append(line)
    for i in spisok:
        lines_1.append(list(filter(None, re.split('\W', i))))
    for word in lines_1:
        for word_1 in word:
            word_1 = str(word_1)
            word_1 += ' '
            lines_2.append(word_1)

    print(lines_2)
