# Сортировака по ключу 

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_numbers.sort(key=lambda x: -x)

print(my_numbers)


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_numbers.sort(key=lambda x: -x if x >= 5 else x)

print(my_numbers)



my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]

my_pairs = list(zip(my_numbers, they_numbers))
print(my_pairs)

my_pairs.sort(key=lambda x: x[0]) # Сортировка по первому элементу
print(my_pairs)


# Словарь с умолчательным значением

goods = [
    ['спички', 12],
    ['соль', 34],
    ['крупа', 56],
    ['спички', 78],
    ['соль', 90],
    ['крупа', 100]
]
good_count = {}
for name, quantity in goods:
    if name in good_count:
        good_count[name] += quantity
    else:
        good_count[name] = quantity
print(good_count)

# Можно с ловлей исключений

goods = [
    ['спички', 12],
    ['соль', 34],
    ['крупа', 56],
    ['спички', 78],
    ['соль', 90],
    ['крупа', 100]
]
good_count = {}
for name, quantity in goods:
    try:
        good_count[name] += quantity
    except KeyError:
        good_count[name] = quantity
print(good_count)

# НО есть решение лучше

from collections import defaultdict

goods = [
    ['спички', 12],
    ['соль', 34],
    ['крупа', 56],
    ['спички', 78],
    ['соль', 90],
    ['крупа', 100]
]
good_count = defaultdict(int) # Возвращает 0, можно с помощью lambda: 0
for name, quantity in goods:
    good_count[name] += quantity
print(good_count)

# Можно с группировать

from collections import defaultdict

goods = [
    ['спички', 12],
    ['соль', 34],
    ['крупа', 56],
    ['спички', 78],
    ['соль', 90],
    ['крупа', 100]
]
good_count = defaultdict(list) # Можно с помощью lambda: [] 
for name, quantity in goods:
    good_count[name].append(quantity)
print(good_count)


# Сортированный словарь

from collections import OrderedDict

my_pets = OrderedDict()
my_pets['собака'] = 'Жучка'
my_pets['мышка'] = 'Норушка'
my_pets['кошка'] = 'Мурка'
my_pets['попугай'] = 'Кеша'
my_pets['рыбка'] = 'Геннадий'
my_pets['таракан'] = 'Дэня'
my_pets['кролик'] = 'Савелий'
print(my_pets)
for k, v in my_pets.items():
    print(k, ':', v)

# Ф-ция reduce

from functools import reduce

my_numbers = [1,2,3,4,5,6]
print(reduce(lambda x, y: x + y, my_numbers))

# 1 + 2 -> 3
# 3 + 3 -> 6
# 6 + 4 -> 10
# И т.д

# Можно найти фактариал числа

n = 10
print(reduce(lambda x, y: x * y, range(1, n + 1)))
