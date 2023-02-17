"""Множественныйе наследование"""

class GrandParent:

    def method(self):
        print("Call for GrandParent")

class ParentOne(GrandParent):

    def method(self):
        super().method()
        print('Call from ParentOne')

class ParentTwo(GrandParent):

    def method(self):
        super().method()
        print("Call from ParentTwo")

class Children(ParentOne, ParentTwo):

    def method(self):
        super().method()
        print('call from child')

obj = Children()
obj.method()
print(obj.__class__.__mro__) # Так можно посмотреть в каком порядоке будут искаться методы 