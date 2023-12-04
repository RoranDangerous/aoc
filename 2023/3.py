from aocd import get_data, submit
from collections import defaultdict 

day = 3
data = get_data(day=day, year=2023).splitlines()

matrix = [list(l) for l in data]

### PART 1 ###
# def has_adjacent_symbol(i, j):
#     adjacent = False

#     if not matrix[i][j].isnumeric() and matrix[i][j] != ".":
#         adjacent = True

#     if i != 0 and not matrix[i-1][j].isnumeric() and matrix[i-1][j] != ".":
#         adjacent = True

#     if i != len(matrix)-1 and not matrix[i+1][j].isnumeric() and matrix[i+1][j] != ".":
#         adjacent = True
    
#     return adjacent

# result = 0
# for i in range(len(matrix)):
#     number = 0
#     attached = False
#     for j in range(len(matrix[i])):
#         if matrix[i][j].isnumeric():
#             number = number * 10 + int(matrix[i][j])
#         elif attached or has_adjacent_symbol(i, j):
#             result += number
#             number = 0
#             attached = False
#         else:
#             number = 0
        
#         attached = attached or has_adjacent_symbol(i, j)

#     result += number if attached else 0



### PART 2 ###
gears = defaultdict(list)

def get_adjacent_star_symbol(i, j):

    if matrix[i][j] == "*":
        return (i, j)

    if i != 0 and matrix[i-1][j] == "*":
        return (i-1, j)

    if i != len(matrix)-1 and matrix[i+1][j] == "*":
        return (i+1, j)
    
    return None

for i in range(len(matrix)):
    number = 0
    gear_coords = None
    for j in range(len(matrix[i])):
        is_gear = gear_coords or get_adjacent_star_symbol(i, j)
        if matrix[i][j].isnumeric():
            number = number * 10 + int(matrix[i][j])
        elif is_gear:
            print(number)
            if number:
                gears[is_gear].append(number)
            number = 0
            gear_coords = None
        else:
            number = 0
        
        gear_coords = gear_coords or get_adjacent_star_symbol(i, j)

    if gear_coords and number:
        gears[is_gear].append(number)

result = 0
for values in gears.values():
    if len(values) == 2:
        result += values[0] * values[1]

submit(result, day=day, year=2023)