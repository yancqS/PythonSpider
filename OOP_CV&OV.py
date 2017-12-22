class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Initializing {})'.format(self.name))
        Robot.population += 1

    def die(self):
        print('{0} is being destoryed'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} was the last one'.format(self.name))
        else:
            print('There are still {0} robot working'.format(Robot.population))

    def say_hi(self):
        print('Gretting, my monster call me {0}'.format(self.name))

    @classmethod  # 类方法既可以由类来引用,也可以由类的实例来引用
    def how_many(cls):
        print('we have {0} robots'.format(cls.population))


droid1 = Robot('R2_001')
droid1.say_hi()
droid1.how_many()  # 由对象来引用

droid2 = Robot('R2_002')
droid2.say_hi()
Robot.how_many()  # 由类来引用

droid1.die()
droid2.die()

Robot.how_many()