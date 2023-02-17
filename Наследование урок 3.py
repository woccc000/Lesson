
class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return "{}: model {}".format(self.__class__.__name__, self.model)

    def operate(self):
        print("Робот ездит по кругу")

class WarRobot(Robot):

    def operate(self):
        print("Робот охраняет военный объект")

class VacuumCleaningRobot(Robot):

    def operate(self):
        print("Робот пылисосит пол")

#r2d2 = WarRobot(model = "R2D2")
#print(r2d2)
#r2d2.operate()

roomba = VacuumCleaningRobot(model = "roomba M2003")
print(roomba)
roomba.operate()


