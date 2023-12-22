import re
import math
from aocd import get_data, submit

day = 8
data = get_data(day=day, year=2023).splitlines()

directions = data[0]
data = data[2:]

# parse
nodes = {}
for l in data:
    start, end = l.split(" = ")
    nodes[start] = re.findall("[0-9A-Z]{3}", end)

### PART 1 ###
# result = 0
# index = 0
# current = "AAA"
# while current != "ZZZ":
#     result += 1

#     move = directions[index % len(directions)]
#     index += 1
    
#     if move == "L":
#         current = nodes[current][0]
#     else:
#         current = nodes[current][1]


### PART 2 ###
start_nodes = list(filter(lambda x: x.endswith('A'), nodes.keys()))

result = 0
index = 0
while True:
    result += 1

    move = directions[index % len(directions)]
    index += 1
    next_move_index = 0 if move == "L" else 1
    for i in range(len(start_nodes)):
        start_nodes[i] = nodes[start_nodes[i]][next_move_index]

    done = True
    for node in start_nodes:
        if not node.endswith("Z"):
            done = False
            break

    if result % 1000000 == 0:
        print(result)
    if done:
        break
    
    if start_nodes[0].endswith("Z"):
        print(result)
        break


submit(math.lcm(17141, 18827, 20513, 12083, 22199, 19951), day=day, year=2023)