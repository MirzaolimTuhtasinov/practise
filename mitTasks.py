# MIT TASK G PYTHON VERSION:
def find_largest(input):
    highest = input[0]

    for i in range(len(input)):
        if highest < input[i]:
            highest = input[i]

    return highest


arr = find_largest([12, 33, 22, 33, 11, 66, 10, 13, 66, 33, -111])
print(f"The highest value is {arr}")
