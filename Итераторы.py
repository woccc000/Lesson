class Family:
    
    def __init__(self) -> None:
        self.dad = 'Вадим'
        self.mom = 'Татьяна'
        self.son = 'Алексей'
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        self.i += 1
        if self.i == 1:
            return f'Папа - {self.dad}'
        elif self.i == 2:
            return f'Мама - {self.mom}'
        elif self.i == 3:
            return f'Я - {self.son}'
        elif self.i == 4:
            return f'Счастливая семья'
        raise StopIteration
    
my_famile = Family()
print(my_famile)
for value in my_famile:
    print(value)

print('Я - Алексей' in my_famile, '\n\n')



# Цифра Фибоначи

def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

fib = fibonacci(n=10)
print(fib)
for value in fib:
    print(value)
print('\n\n')


# Итератор последовательности фибоначи

class Fibonacci:

    def __init__(self, n) -> None:
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self
    
    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration
            self.a, self.b = self.b, self.a + self.b
        return self.a
    

fib_iterator = Fibonacci(n = 100000)
#print(fib_iterator)

#for value in fib_iterator:
#    print(value)

print(13 in fib_iterator)