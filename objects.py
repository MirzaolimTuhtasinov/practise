''' OBJECTS
    (1) What is the object
    (2) Iterable objects & RANGE
    (3) DICTIONARY
    (4) Error handling system
'''

# print("=== What is the object ===")
# # An object has state and method properties.
# # Everything is object in Python!

# import array  # package/module
# import math
# from math import ceil, asin

# print(type("Hello World!"))
# print(type(222))
# print(type(True))
# print(type(array))
# print(type(math))

# # Paradigms > Functional Programmming & OOP
# # OOP 4 CONCEPTS > Abstaction | Encapsulation | Inheritence | Polymorphism
# result1 = math.ceil(97.7)  # CALL
# print("result1:", result1)

# result2 = ceil(99.3)
# print("result2:", result2)

print("=== Error handling system ===")
car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print("passed here")
    result = car_dict["origin"]
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")

print('===================')
try:
    print("passed here")
    result = car_dict["year"]
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")

print('===================')

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
except AttributeError as err:
    print("No speed found:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")

print('===================')

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
except (KeyError, AttributeError) as err:
    print("ERROR:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")


print('===================')

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
except Exception as err:
    print("GENERAL ERROR:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")
