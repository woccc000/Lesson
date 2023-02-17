class Live():

    def __init__(self):
        self.money = 500
        self.name = "denchik"
        self.food = 100
        self.day = 365

    def __str__(self):
        return "Имя: {}, Еда: {}, День: {}".format(self.name, self.food, self.day)

    def data(self, day):
        self.month = self.day // 12
        self.wook = self.month // 4 - 0,5 


    """def food(self, food, day):
        while self.food != 0:
            self.day = self.day - 1
            self.food = self.food - 50

            if self.food <= 10:
                self.money -= 100
                self.food += 50
                return "Сходил в магазин"

            elif self.money < 100:
                self.day -= 1
                self.money += 125
                return "Сходил на работу" """

    def work(self, money, day):
        pass
        


men = Live()
print(men)
