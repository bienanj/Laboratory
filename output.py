from student import Student
from teacher import Teacher
from grade import Grade
from load import Load

#Student Output
print()
Stud = Student('123','Surname','Fname','Midname','Student','2','BSCS','A')
print(Stud.name())
print(Stud.getYrCourseSec())
print()
print('------------------------------')

#STUDENT OUTPUT WITH GRADE
Grade1 = Grade(' 90','99','94','92')
Grade1.type = 'Student'
Grade1.id = '123'
Grade1.last_name = 'Surname'
Grade1.first_name = 'Fname'
Grade1.middle_name = 'Midname'
Grade1.year = '2'
Grade1.course = 'BSCS'
Grade1.section = 'A'

print(Grade1.name())
print(Grade1.getYrCourseSec())
print('------------------------------')
print(Grade1.getGrade())
print('Average: ' + str(Grade1.getAverage()))
print()
print('------------------------------')

#TEACHER OUTPUT
Teach = Teacher('Teacher','1234','Surname','Fname','Midname','CEIT','Dean')
print(Teach.name())
print(Teach.getDepartment())
print(Teach.getPosition())

Load = Load('English','Math','Science','Filipino')
print('------------------------------')
print('Load: ' + Load.getSubject())