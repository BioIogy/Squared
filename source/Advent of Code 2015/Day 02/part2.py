# Python 3.x

def total_ribbon(dimensions):
    ribbon = 0
    for dimension in dimensions:
        length, width, height = (int(number) for number in dimension.split('x'))
        string = [length, width, height]
        ribbon += 2 * (sum(string) - max(string)) + length * width * height
    return ribbon

with open('input.txt') as file:
    print(total_ribbon([line.rstrip('\n') for line in file.readlines()])) # 1598415