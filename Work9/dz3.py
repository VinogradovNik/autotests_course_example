# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
f = open('test_file/task_3.txt', 'r', encoding='utf-8')
summa = 0
list_products = []
for i in f.readlines():
    if i != '\n':
        summa += int(i)
    else:
        list_products.append(summa)
        summa = 0

three_most_expensive_purchases = sum(sorted(list_products, reverse=True)[0:3])
assert three_most_expensive_purchases == 202346