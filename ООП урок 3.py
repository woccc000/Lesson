class BackPack():
    """Рюкзак"""

    def __init__(self, gift = None): # gift уже лежит в параметре класса
        self.content = []
        if gift is not None:         # Если gift не пустой то
            self.content.append(gift)# Добавляем его в список


        """Добавление"""
    def add(self, item):
        self.content.append(item)
        print(u"Вы положили: ", item)

        """Содержимое"""
    def __str__(self):
        return "Рюкзак: " + ", ".join(self.content)

    def __bool__(self):
        return self.content != []

    def __len__(self):
        return len(self.content)

    
    
    #def __del__(self):               # Удаление объекта 
        #self.content = None          # Очистили список, разоравали связи с Объктом
        #print("Прощай мир...")
    
my_backpack = BackPack()
my_backpack.add(item = "Ноутбук")
#print(bool(my_backpack), len(my_backpack))
if my_backpack:                       # Вызывается логический тип, булевое значение объекта
    print("Мой рюкзак не пуст")
    print("В нем лежит ", len(my_backpack), " предметов")
else:
    print("Рюкзак пустой")