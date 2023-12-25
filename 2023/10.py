from aocd import get_data, submit

day = 10
data = get_data(day=day, year=2023).splitlines()
data = '''.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...'''.splitlines()

start = None
for i in range(len(data)):
    if start:
        break

    for j in range(len(data[i])):
        if data[i][j] == "S":
            start = (i, j)
            break


### PART 1 ###
# location = start
# steps = 0
# direction = ">"
# while True:
#     steps += 1

#     if direction == ">":
#         location = (location[0], location[1]+1)
#         next = data[location[0]][location[1]]
#         if next == "7":
#             direction = "v"
#         elif next == "J":
#             direction = "^"
#     elif direction == "<":
#         location = (location[0], location[1]-1)
#         next = data[location[0]][location[1]]
#         if next == "F":
#             direction = "v"
#         elif next == "L":
#             direction = "^"

#     elif direction == "^":
#         location = (location[0]-1, location[1])
#         next = data[location[0]][location[1]]
#         if next == "F":
#             direction = ">"
#         elif next == "7":
#             direction = "<"
#     elif direction == "v":
#         location = (location[0]+1, location[1])
#         next = data[location[0]][location[1]]
#         if next == "J":
#             direction = "<"
#         elif next == "L":
#             direction = ">"

#     if next == "S":
#         break
# result = steps / 2


### PART 2 ###
pipes = [["." for _ in range(len(data[0]))] for _ in range(len(data))]
location = start
steps = 0
direction = ">"
while True:
    steps += 1
    pipes[location[0]][location[1]] = direction

    if direction == ">":
        location = (location[0], location[1]+1)
        next = data[location[0]][location[1]]
        if next == "7":
            direction = "v"
        elif next == "J":
            direction = "^"
    elif direction == "<":
        location = (location[0], location[1]-1)
        next = data[location[0]][location[1]]
        if next == "F":
            direction = "v"
        elif next == "L":
            direction = "^"
    elif direction == "^":
        location = (location[0]-1, location[1])
        next = data[location[0]][location[1]]
        if next == "F":
            direction = ">"
        elif next == "7":
            direction = "<"
    elif direction == "v":
        location = (location[0]+1, location[1])
        next = data[location[0]][location[1]]
        if next == "J":
            direction = "<"
        elif next == "L":
            direction = ">"

    if next == "S":
        break

print("\n".join(["".join(row) for row in pipes]))
# submit(result, day=day, year=2023)