class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        new_vector = Vector2(self.x + other.x, self.y + other.y)
        return new_vector

    def subtract(self, other):
        new_vector = Vector2(self.x - other.x, self.y - other.y)
        return new_vector

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

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

students = [
    Student("Jake", 19, "Computer Science"),
    Student("Jeff", 20, "Psychology"),
    Student("Amy",  18, "BAIT"),
    Student("Isha", 21, "Computer Science")
]