class BackPack:

    def __init__(self,gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)

    """Сложение двух объктов"""
    def __add__(self, other):
        new_obj = BackPack()                        # Создаем новый объект рюкзак 
        new_obj.content.extend(self.content)
        if isinstance(other, BackPack):             # Если содержимое есть в рюкзаке то
            new_obj.content.extend(other.content)   # Добавляем его в новый рюкзак
        else:                                       
            new_obj.content.extend(other)           # Добавляем новый список
        return new_obj                              # Содержимое нового рюкзака из первого и второго объекта


    """Сравнение"""
    """def __eq__(self,other):                         
        return self.content == other.content"""






my_backpack = BackPack(gift='Бутер')
bro_backpack = BackPack(gift='телефон')

new_backpack = my_backpack + ["Яблоко", "банан"]

print(new_backpack)

"""
if my_backpack == bro_backpack:
    print("Как мы похожи")

# Вывод: "Как мы похожи"

if BackPack.__eq__(self = my_backpack, other = bro_backpack):
    print("Как мы похожи")

# Вывод: "Как мы похожи"""