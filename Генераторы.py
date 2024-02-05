def fibonacci_v1(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


print("\n\n", '#' * 20, '\n новый код\n')


# Оператор yield(Производить, выдавать значение)
def fibonacci_v2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# По генератору можно проходиться один раз!!!
fib = fibonacci_v2(n=10)
print(fib)
for value in fib:
    print(value)

fib2 = fibonacci_v2(n=10)
print(13 in fib2) 


print("\n\n", '#' * 20, '\n новый код\n')


# Можно создать бесконечный генератор 'Список' значений
def fibonacci_v3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for value in fibonacci_v3():
    print(value)
    if value > 10 ** 6:
        break


print("\n\n", '#' * 20, '\n новый код\n')

# Можно использовать return - он воспринимается, как завершение итерирования
def fibonacci_v4():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        if a > 10 ** 30:
            return 
        
for val in fibonacci_v4():
    print(value)


print("\n\n", '#' * 20, '\n новый код\n')


# Прирывание вложенных циклов 

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

can_continue = True
for x in list_1:
    for y in list_2:
        result = x * y
        print(x, y, result)
        if result == to_find:
            print('found!!!')
            can_continue = False
            break
    if not can_continue:
        break

