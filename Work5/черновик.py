my_list = [('Мартин', 5, 'Алексей', 'Егоров'),
('Фродо', 3, 'Анна', 'Самохина'),
('Вася', 4, 'Алексей', 'Егоров')]
dict1 = {(element[0], str(element[1])): (element[2], element[3]) for element in my_list}

spisok = []
spisok_str = []
index1 = 0
our_str = ''
for key, value in dict1.items():
    if value not in spisok:
        str1 = ' '.join(value) + ':' + ' ' + ' '.join(key)
        spisok.append(value)
        spisok_str.insert(index1, str1)
        index1 += 1

    else:
        str2 = '; ' + ' '.join(key)
        spisok_str[spisok.index(value)] += str2
for element in spisok_str:
    our_str += element + '\n'
print(our_str)
















