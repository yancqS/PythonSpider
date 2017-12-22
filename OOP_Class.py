class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('hello god', self.name)


p = Person('yancq')
p.say_hi()