import re
spisok = []
list_1 = []
list_2 = []
list_3 = []
first_words2 = []
first_words3 = []

def first(list_1, list_2):
    with open('input.txt', 'r+') as file:
        lines = file.readlines()
        for j in lines:
            line = j[:-1]
            line += ' '
            spisok.append(line)
        # print(spisok)  # 1-2 пункты задания
        for i in spisok:
            list_1.append(re.split(' ', i[:-1]))
            list_2.append(list(filter(None,  re.split('\W', i))))

    return list_1, list_2  # со знаками препинания, чисто слова и ни чего больше
first(list_1, list_2)

list_of_words = []
for j in list_2:
    for a in j:
        list_of_words.append(a)
print(list_of_words)         # список слов по порядку
words = set(list_of_words)   # не повторяющиеся слова
print(words)
first_words = []                 # стартовые слова ,заглавные
for q in words:
    if q[0] == q[0].upper():
        first_words.append(q)
print(first_words)
for n in range(len(list_of_words)):
    for ken in first_words:
        if list_of_words[n] == ken:
            pass
for i in range(len(first_words)):
    for t in range(len(list_of_words)):
        if list_of_words[t] == first_words[i] and list_of_words[t+1] != first_words[i] and list_of_words[t+1][0] not in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            first_words2.append(list_of_words[t+1])
        elif list_of_words[t] == first_words[i] and list_of_words[t+1] != first_words[i] and list_of_words[t+1][0] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            first_words2.append('.')
print(first_words2)

for i in range(len(first_words2)):
    if first_words2[i] != '.':
        for t in range(len(list_of_words)):
            if list_of_words[t] == first_words2[i] and list_of_words[t + 1] != first_words2[i] and \
                    list_of_words[t + 1][0] not in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                        first_words3.append(list_of_words[t + 1])
            elif list_of_words[t] == first_words2[i] and list_of_words[t + 1] != first_words2[i] and \
                    list_of_words[t + 1][0] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                        first_words3.append('.')
    else:
        first_words3.append('.')

print(first_words3)
