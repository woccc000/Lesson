#try:
#    truba = a + b
#   truba = 10 / 0
#except ZeroDivisionError: # Указываем точный класс ошибки, или классов ошибок
#    # Ловим ошибку
#    print("Что-то пошло не так!!!")
#except NameError: # Можно указывать сколько угодно except
#    print("Ошибка, такой переменной не существует")
#try:
#    file = open('blabla.txt')
#except OSError as exc:
#    print(f'Вот что пошло не так - {exc}, параметры - {exc.args}')



#def f1(numbers):
#    return total / numbers
#
#def f2():
#    sumn = 0
#    for i in range(2, -1, -1):
#        try:
#            sumn += f1(numbers=i)
#            print(sumn)
#        except ZeroDivisionError as exc:
#            print(f'Что-то пошло не так в f1 - {exc}')
#    return sumn / 0
#
#try:
#    f2()
#except ZeroDivisionError as exc:
#    print(f'Что-то пошло не так в f2 - {exc}')



"""Обобщенный ошибки"""
f = None
try:
    f = open('mylife.txt', 'r')
    s = f.readline()
    i = int(s.strip())
except IOError as exc:
    print("I/O error", exc)
except ValueError as exc:
    print('Не могу преобразовать данные в целое!')
except Exception as exc:
    print(f'Неожиданная ошибка - {exc}')
else:
    print('прочитано i = ', i)
finally:
    if f is not None:
        f.close()

