from teacher import Teacher

class Load(Teacher):

    def __init__(self, Subject1, Subject2, Subject3, Subject4):
        self.Subject1 = Subject1
        self.Subject2 = Subject2
        self.Subject3 = Subject3
        self.Subject4 = Subject4

    def getSubject(self):
        return f'{self.Subject1}. {self.Subject2}. {self.Subject3}, {self.Subject4}'
        