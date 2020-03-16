with open('input.txt', 'r+') as file:
    lines = file.readlines()
    for k in lines:
        lines_1.append(list(filter(None, re.split('\W', k))))
    print(lines_1)