import string
import re
spisok = []
list_1 = []
list_2 = []
with open('input.txt', 'r+') as file:
    lines = file.readlines()
    for j in lines:
        line = j[:-1]
        line += ' '
        spisok.append(line)
    print(spisok)  # 1-2 пункты задания
    for i in spisok:
        list_1.append(re.split(' ', i[:-1]))
        list_2.append(list(filter(None,  re.split('\W', i))))
    print(list_1)   # со знаками препинания
    print(list_2)   # чисто слова и ни чего больше



