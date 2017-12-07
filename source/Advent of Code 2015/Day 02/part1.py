# Python 3.x

def total_paper(dimensions):
    paper = 0
    for dimension in dimensions:
        length, width, height = (int(number) for number in dimension.split('x'))
        areas = [length * width, width * height, height * length]
        paper += 2 * sum(areas) + min(areas)
    return paper

with open('input.txt') as file:
    print(total_paper([line.rstrip('\n') for line in file.readlines()])) # 1598415