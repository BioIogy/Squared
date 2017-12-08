# Python 3.x

CHAR_GREATER_THAN = '>'
CHAR_LESS_THAN ='<'
CHAR_CIRCONFLEXE = '^'
CHAR_V = 'v'

def houses_with_present(moves):
    grid = [['0,0'], ['0,0']]
    for index, move in enumerate(moves):
        grid_index = int(index % 2 == 0)
        x, y = [int(x) for x in grid[grid_index][-1].split(',')]
        if move == CHAR_GREATER_THAN:
            x += 1
        elif move == CHAR_LESS_THAN:
            x -= 1
        elif move == CHAR_CIRCONFLEXE:
            y += 1
        elif CHAR_V:
            y -= 1
        grid[grid_index].append(",".join((str(x), str(y))))
    return len(set(grid[0] + grid[1]))

with open('input.txt') as file:
    print(houses_with_present(file.read())) # 2341