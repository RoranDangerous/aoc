from aocd import get_data, submit
import re

day = 2
data = get_data(day=day, year=2023).splitlines()

### PART 1 ### 
# possible_cubes = {
#     "blue": 14,
#     "red": 12,
#     "green": 13
# }

# result = 0
# for i in range(len(data)):
#     cubes = re.findall("(\d* (?:blue|green|red))", data[i])
#     possible = True
#     for cube in cubes:
#         d = cube.split(" ")
#         if possible_cubes[d[1]] < int(d[0]):
#             possible = False
#             break
    
#     if possible:
#         result += i + 1


### PART 2 ###
result = 0
for i in range(len(data)):
    min_cubes = { "blue": None, "green": None, "red": None }
    cubes = re.findall("(\d* (?:blue|green|red))", data[i])
    for cube in cubes:
        d = cube.split(" ")
        if min_cubes[d[1]] is None or min_cubes[d[1]] < int(d[0]):
            min_cubes[d[1]] = int(d[0])
    
    r = 1
    for num in min_cubes.values():
        r *= num
    
    result += r


submit(result, day=day, year=2023)