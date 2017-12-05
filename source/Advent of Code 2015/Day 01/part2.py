# Python 3.x

LEFT_PARENTHESIS = '('

def first_basement_instruction(instructions):
    "Return the index of instructions (plus one) when floor turns negative."
    floor = 0

    for index, instruction in enumerate(instructions):
        if instruction == LEFT_PARENTHESIS:
            floor += 1
        else :
            floor -= 1

        if floor < 0:
            return index + 1

with open('input.txt') as file:
    print(first_basement_instruction(file.read())) # 1771