from aocd import get_data, submit

day = 6

### PART 1 ###
# data = [[52, 426], [94, 1374], [75, 1279], [94, 1216]]
# result = 1
# for race in data:
#     time, record_distance = race
#     count = 0
#     for t in range(time):
#         distance = t * (time - t)
#         if distance > record_distance:
#             count += 1

#     if count:
#         result *= count

### PART 2 ###
data = [[52947594, 426137412791216]]

result = 1
for race in data:
    time, record_distance = race
    count = 0
    for t in range(time):
        distance = t * (time - t)
        if distance > record_distance:
            count += 1

    if count:
        result *= count

submit(result, day=day, year=2023)