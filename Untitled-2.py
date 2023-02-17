"""Метод Super"""

class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return "{}: model {}".format(self.__class__.__name__, self.model)

    def operate(self):
        print("Робот ездит по кругу")

class VacuumCleaningRobot(Robot):

    def __init__(self, model):
        super().__init__(model=model)
        self.dust_bug = 0

    def operate(self):
        print("Робот пылисосит пол, заполненость мешка для пыли", self.dust_bug)

class WarRobot(Robot):

    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self):
        super().operate()
        print("Робот охраняет военный объект, с помощью", self.gun)

class SubmarineRobot(WarRobot):

    def operate(self):
        super().operate() 
        print("Охрана ведется под водой")

rc_submarin = SubmarineRobot(model = "W30F23", gun = "Ракеты")
print(rc_submarin)
rc_submarin.operate()

#roomba = VacuumCleaningRobot(model = "roomba M2003")
#print(roomba)
#roomba.operate()
