class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        new_vector = Vector2(self.x + other.x, self.y + other.y)
        return new_vector
        # self.x += other.x
        # self.y += other.y

    def subtract(self, other):
        new_vector = Vector2(self.x - other.x, self.y - other.y)
        return new_vector

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

"""
Add two vectors (a and b) and take the result as c, then compute the distance 
from  c to a!
"""

def vec2_example():
    a = Vector2(4,0)

    b = Vector2(2,3)

    c = a.add(b)

    dist = c.distance(a)
    print("The distance from c to a is",dist)

# vec2_example()

class Student():
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        self.friends = []

    def add_friend(self, other):
        self.friends.append(other)

    def is_friends_with(self, other):
        return other in self.friends

def stud_example():
    """Write a program that prints out the name of the oldest student!"""
    students = [
        Student("Jake", 19, "Computer Science"),
        Student("Jeff", 20, "Psychology"),
        Student("Amy",  18, "BAIT"),
        Student("Isha", 21, "Computer Science")
    ]

    oldest_student = students[0]

    students[0].add_friend(students[1])
    students[1].add_friend(students[0])

    students[3].add_friend(students[0])
    students[0].add_friend(students[3])    

    for student in students:
        if student.age > oldest_student.age:
            oldest_student = student

    print("The oldest student is",oldest_student.name)
    print("They have ",len(oldest_student.friends))

stud_example()