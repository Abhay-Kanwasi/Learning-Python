# Programming Paradigms

"""
- Paradigm means the principle according to which a program is organized to carry out a given task.
- Python supports all three programming paradigms --Structured prgoramming, functional and object oriented.
- OOP encourages creation and interaction of object.
"""

# What are classes and objects ?

"""
class: a class contains data and methods that can access or manipulate data. Because of this a class let us bundle data and functionality together.
object: an object is an instance of a class.

public and private memebers.
"""


class Employee:
    def set_data(self, name='', age=0, salary=0):
        self._name = name
        self._age = age
        self._salary = salary

    def __init__(self, name='', age=0, salary=0):
        self._name = name
        self._age = age
        self._salary = salary

    def display_data(self):
        print(self._name)
        print(self._age)
        print(self._salary)

employee1 = Employee()
# employee2 = Employee()

# employee1.set_data("John", 25, 50000)   
employee1.display_data()

# print(Employee.__name__)

# if __name__ == "__main__":
#     print(type(employee1))


# class Human:
#     "Human class implementation"
#     def work(self):
#         print("I am working")

#     def eat(self):
#         print("I am eating")

# h = Human() # object
# h.work() # calling method using object | work(h)

# print(Human.__doc__)
