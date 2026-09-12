'''FUNCTIONS
(1) Define vs Call
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''

print("==== DEFINE VS CALL ====")
# build in function > print() type() ...
# function - reusable block of code!
# instead of block {} in JAVA, Python uses indentation!

# DEFINE - build

# def greet(a):
#     pass


def greet(a):
    print(f"How do you do, {a}?")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute
result1 = greet("Joseph")
print("====1")
greet("Joseph")
print("====2")
print("result1:", result1)

result2 = greeting("Martin")
print("====3")
print("result2:", result2)
