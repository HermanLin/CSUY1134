'''
class Employee:
    #constructor
    #initialize values of obj
    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age
    #representation
    #returns something to represent the obj
    def __repr__(self):
        return 
    #length
    def __len__(self):
        return self.age
    #stringify
    #str representation needed for print()
    def __str__(self):
        return "Josh is " + str(self.age) + " years old"


josh = Employee("Josh", "occup", 27)
print(josh)
'''
'''
class Student:
    def __init__(self, name = "student", age = 18):
        self.name = name
        self.age = age
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print("Removed Course:", course)
        else:
            print("Course Not Found:", course)

    def __str__(self):
        info = "Name: " + self.name
        info += "\nAge: " + str(self.age)
        info += "\nCourses: " + " , ".join(self.courses)
        return info + "\n"
    
peter = Student(16)
print(peter.name, peter.age)

peter = Student("Peter Parker")
print(peter.name, peter.age)

peter = Student(age = 16)
print(peter.name, peter.age)

peter.name = "Peter Parker"
print(peter)

peter.add_course("Algebra")
peter.add_course("Chemistry")
print(peter)

peter.add_course("Physics")
peter.remove_course("Spanish")

flash = Student("Flash Thompson")
flash.courses = peter.courses
flash.add_course("Economics")
peter.remove_course("Chemistry")
print(peter.courses)
print(flash.courses)

peter.name, flash.name = flash.name, peter.name
print(peter.name, peter.age)
print(flash.name, flash.age)
'''

class Polynomial:
    def __init__(self, lst = []):
        poly = ""
        if len(lst) != 0:
            for x in range(len(lst)):
                if lst[x] != 0:
                    
        else:
            poly = "0"