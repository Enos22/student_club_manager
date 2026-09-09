class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi! My name is {self.name} and I am {self.age} years old.")

#Test Example
student1 = Student("Alice", 18)
student2 = Student("Njeri", 19)
student1.introduce()
student2.introduce()

#Part B
class Club:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, student):
        self.members.append(student)

    def show_members(self):

        print (f"Members of {self.name}: ")
        for student in self.members:
            print(f"{student.name}")

#Test Example
gaming_club = Club( "Gaming Club")
robotics_club = Club("Robotcs Club")

gaming_club.add_member(student1)
robotics_club.add_member(student2)

gaming_club.show_members()
robotics_club.show_members()
