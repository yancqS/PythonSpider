class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initializing SchoolMember:{})'.format(self.name))

    def tell(self):
        print('Name:"{}", age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initializing Teacher:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{}"'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, mark):
        SchoolMember.__init__(self, name, age)
        self.mark = mark
        print('(Initializing Student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('mark:"{}"'.format(self.mark))


t = Teacher('snake', 30, 300000)
s = Student('superman', 21, 98)

print()

members = [t, s]
for member in members:
    member.tell()