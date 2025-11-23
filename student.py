
class student:
    def __init__(self, name, age, major, grade):
        self.name = name
        self.age = age
        self.major = major
        self.grade = grade
    
    def on_honor_roll(self):
        if self.grade >= 6.0:
            return True
        else:
            return False