import warnings

def greet_person(person_name):
    if person_name == 'Robert':
        warnings.warn('Опять этот Роберт')
    print(f'Твое имя {person_name}')

greet_person('Robert')
print("Выполнение продолжается")
for i in range(10):
    print(f'i={i}')