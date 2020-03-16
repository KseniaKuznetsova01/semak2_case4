import string
import re
lines_1 = []
lines_2 = []

with open('input.txt', 'r+') as file_1:
    lines = file_1.readlines()
    print(lines)

    lines = file_1.readlines()
    for k in lines:
        lines_1.append(list(filter(None, re.split('\W', k))))
    print(lines_1)