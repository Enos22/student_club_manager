# Context
Your school has several clubs such as Gaming Club, Robotics Club, Football Club and Music Club.
Students can join these clubs. Instead of saving only a student name inside a club, you will save the actual
Student object. This lets the Club object keep a relationship with each Student object.
Relationship idea
Student -> joins -> Club. A Club can store several Student objects in its members list. Because the list
contains objects, the club can later access information such as student.name or even call
student.introduce().

# Part A - Student
1. Create a Student class with name and age attributes.
2. Create an introduce() method that prints a short introduction.
Expected interaction
student1.introduce() might print: Hi! My name is Alice and I am 18 years old.

# Part B - Club
1. Create a Club class with a name attribute.
2. Create an empty members list when the club is created.
3. Create add_member(student) to add a Student object to the members list.
4. Create show_members() to display the names of everyone in the club.

# Expected interaction
gaming_club.add_member(student1) should print: Alice joined Gaming Club!
Python OOP Practice Workshop | Beginner Level | 6
Starter Code
class Student:
 def __init__(self, name, age):
 pass
 def introduce(self):
 pass
class Club:
 def __init__(self, name):
 self.name = name
 self.members = []
 def add_member(self, student):
 pass
 def show_members(self):
 pass
student1 = Student("Alice", 18)
student2 = Student("Brian", 19)
student3 = Student("Faith", 18)
gaming_club = Club("Gaming Club")
robotics_club = Club("Robotics Club")
gaming_club.add_member(student1)
gaming_club.add_member(student2)
robotics_club.add_member(student3)
gaming_club.show_members()
robotics_club.show_members()

# Checkpoint Questions
 Why is members a list?
 What exactly are you adding to members: a name string or a Student object?
 Can one Club object contain several Student objects?
 If the list contains Student objects, how can you display each student name?
