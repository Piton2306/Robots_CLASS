class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('Инициализация {0}'.format(self.name))
        Robot.population += 1

    def dell(self):
        '''Унечтожение роботов'''
        print(('{0} Уничтожается!').format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print(("{0} был посдедним").format(self.name))
        else:
            print(('Осталось {0} работающих робатов').format(Robot.population))

    def SayHi(self):
        """Приветствие робота.

        Да они это могут"""
        print("ПРиветствую! Мои хозяева называют меня {0}".format(self.name))

    def HowMany():
        """Выыодит численность роботов"""

        print(("У нас {0} роботов").format(Robot.population))


droid1 = Robot('R2-D2')
droid1.SayHi()
Robot.HowMany()
print()
droid2 = Robot("ROBA")
droid2.SayHi()
Robot.HowMany()
print("\nВыполнили задание!")
print('Унечтожение')
droid1.dell()
print()
droid2.dell()
Robot.HowMany()
