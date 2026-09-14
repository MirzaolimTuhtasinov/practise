'''CLASS
    (1) What is the class
    (2) Ordinary vs static properties
    (3) Special methods
'''

# print("=== What is the class ===")
# # class - blueprint for object creation!
# # structure > state constructor method


# class Person():
#     # state
#     message = "class state property"

#     # constructor
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # method
#     def introduce(self):
#         print(f"{self.name} says: How do you do?")

#     def say_age(self):
#         print(f"{self.name} says 'I am {self.age}")


# person1 = Person("Spider", 20)
# person2 = Person("Martin", 35)

# # ordinary state property
# print("name:", person1.name)

# # ordinary method
# person1.introduce()
# person2.say_age()

print("=== Ordinary vs static properties ===")


class Person():
    # state
    message = "static state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do?")

    def say_age(self):
        print(f"{self.name} says 'I am {self.age}")

    @classmethod
    def explain(cls):
        print("static method property executed!")


# static state
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()
