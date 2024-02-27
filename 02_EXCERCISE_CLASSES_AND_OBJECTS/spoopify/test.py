class Test:
    information = []

    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self):
        Test.information.append(self.name)
        return f"{self.name} is added to the list"


student_1 = Test('Ivan')
student_2 = Test('Angel')
student_3 = Test('Karina')
Test.add_student(student_1)
Test.add_student(student_2)
Test.add_student(student_3)
print(', '.join(Test.information))
