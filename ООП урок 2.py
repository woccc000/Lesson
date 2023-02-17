class BackPack():
    
    def add(self, item):
        """Положем в рюкзак"""
        print("\t Рюкзак \n","Вы положили: ", item)
        self.content = item

my_backpack = BackPack()
laptop = "Asus laptop"
print(my_backpack.add(item = laptop))


my_backpack_1 = BackPack()
my_backpack_1.add(item = "Учебник")

print("В рюкзаке есть:\n",my_backpack.content, ", ", my_backpack_1.content)