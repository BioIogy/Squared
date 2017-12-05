# Python 3.x

def what_floor(instructions):
    "Return absolute value of difference between parenthesis occurences."
    return abs(instructions.count("(") - instructions.count(")"))

with open('input.txt') as file:
    print(what_floor(file.read())) # 138