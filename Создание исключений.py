#def greet_person(person_name):
#    """
#    say hello
#    """
#    if person_name == 'Robert':
#        raise BaseException('ТЫ РОБЕРТ?')
#    print(f'Добро пожаловать {person_name}!')
#
#pers = 'Robert'
#pers_1 = 'DEnchik'
#
##greet_person(pers)
#greet_person(pers_1)

#try:
#    raise NameError('Привет Там')
#except NameError as exc:
#    print(f'Исключение типа - {type(exc)}, пролетело мимо! Его параметры - {exc.args}')
#    raise TypeError("И тут привет")


class DivisionError(Exception):

    def __init__(self, message, input_data = None):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return self.message
    
def division(a, b):
    if a < b:
        raise DivisionError("Нельзя делить меньшее на большее", input_data=dict(a=a, b=b))
    return a / b

try:
    division(1,2)
except DivisionError as exc:
    print(f'Поймано исключение типа - {exc}, входные данные - {exc.input_data}')
        