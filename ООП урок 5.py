"""Различие атрибутов класса и экземпляра"""

from random import randint, choice

class Lemming:
    
    # Можно определять атрибуты на уровне класса, тогда они 'Привязываются' к классу
    total, names = 0, ["Анна", "Вася", "Маша", "Саша", "Миша", "Денчик", "Макс"]
    names_count = len(names)
    some_text = 'Варкалось, хливкие хорьки пырились по наре...'
    some_var = some_text + names[-1]

    def __init__(self):
        Lemming.total += 1
        self.name = choice(Lemming.names)

    def __str__(self):
        return 'Lemming ' + self.name

    def check_class_attrs(self):
        print("Lemminf.total", Lemming.total)
        print("Lemminf.names", Lemming.names)
        print("Lemminf.names_count", Lemming.names_count)
        print("Lemminf.some_text", Lemming.some_text)
        print("Lemminf.some_var", Lemming.some_var)


new_lemming = Lemming()
print("Lemminf.total", Lemming.total)
print("Lemminf.names", Lemming.names)
print("Lemminf.names_count", Lemming.names_count)
print("Lemminf.some_text", Lemming.some_text)
print("Lemminf.some_var", Lemming.some_var)
new_lemming.check_class_attrs()

