print("\n\n", '#' * 20)



def adder(*args):
    res = 0
    for number in args:
        res += number
    return res

def multiplier(*args):
    res = 1
    for number in args:
        res *= number
    return res

def process_numbers(numbers, handler):
    result = handler(*numbers)
    print(f'Получилось {result}')

my_numbers = [3,1,4,1,5,9,2,6]
process_numbers(numbers=my_numbers, handler=adder)
process_numbers(numbers=my_numbers, handler=multiplier)



print("\n\n", '#' * 20)

# Ф-ция map

def mul_by_2(x):
    return x * 2

def mul_by_3(x):
    return x * 3

my_numbers = [3,1,4,1,5,9,2,6]

result = map(mul_by_2, my_numbers)
print(result)

print(list(result))
result = map(mul_by_3, my_numbers)
print(list(result))

print("\n\n", '#' * 20)


# Ф-ция filter

def mul_by_2(x):
    return x * 2

def mul_by_3(x):
    return x * 3

def is_odd(x):
    return x % 2

my_numbers = [3,1,4,1,5,9,2,6]

result = filter(is_odd, my_numbers)
print(result)
print(list(result))

# Можно совместить - получаются вложенные последовательности обработки

result = map(mul_by_3, filter(is_odd, my_numbers))
print(list(result))

result = sum(map(mul_by_3, filter(is_odd, my_numbers)))
print(result)