from person import Person

class Teacher(Person):
    def __init__(self, last_name, first_name, middle_name, type, Department, Position):
        self.Department = Department
        self.Position = Position

        super().__init__(self, id. last_name, first_name, middle_name, type)

    def __str__(self):
        return super().__str__()

    def getDepartment(self):
        return self.Department

    def getPosition(self):
        return self.Position
