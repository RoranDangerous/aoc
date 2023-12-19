from aocd import get_data, submit

day = 5
data = get_data(day=day, year=2023).splitlines()

### PART 1 ###

# # parsing
# seeds = []
# index = -1
# maps = [[], [], [], [], [], [], []]
# for l in data:
#     if l.startswith("seeds:"):
#         seeds = [int(n) for n in l.strip("seeds: ").split(" ")]
#         continue

#     if l == "":
#         continue
    
#     if "map:" in l:
#         index += 1
#         continue

#     maps[index].append([int(n) for n in l.split(" ")])

# def process_map(m):
#     initial_seeds = [*seeds]
#     for i in range(len(initial_seeds)):
#         for row in m:
#             if initial_seeds[i] >= row[1] and initial_seeds[i] < row[1] + row[2]:
#                 seeds[i] = row[0] + initial_seeds[i] - row[1]

# for m in maps:
#     process_map(m)

# result = min(seeds)


### PART 2 ###

# parsing
seeds_raw = []
seeds = []
index = -1
maps = [[], [], [], [], [], [], []]
for l in data:
    if l.startswith("seeds:"):
        seeds_raw = [int(n) for n in l.strip("seeds: ").split(" ")]
        continue

    if l == "":
        continue
    
    if "map:" in l:
        index += 1
        continue
    
    maps[index].append([int(n) for n in l.split(" ")])

i = 0
while i < len(seeds_raw):
    seeds.append((seeds_raw[i], seeds_raw[i] + seeds_raw[i+1] - 1))
    i += 2

def process_map(m):
    seeds_untouched = [*seeds]
    seeds_new = []
    for row in m:
        seeds_untouched_new = []
        for seed in seeds_untouched:
            if seed[0] < row[1]:
                seeds_untouched_new.append([seed[0], min(row[1] - 1, seed[1])])

                if seed[1] >= row[1]:
                    end = min(row[1] + row[2] - 1, seed[1])
                    seeds_new.append([
                        row[0],
                        end - row[1] + row[0]
                    ])

            elif seed[0] < row[1] + row[2]:
                end = min(row[1] + row[2] - 1, seed[1])
                seeds_new.append([
                    seed[0] - row[1] + row[0],
                    end - row[1] + row[0]
                ])

            if seed[1] >= row[1] + row[2]:
                seeds_untouched_new.append([max(row[1] + row[2], seed[0]), seed[1]])
        seeds_untouched = seeds_untouched_new
    
    seeds_new += seeds_untouched

    return seeds_new

for m in maps:
    seeds = process_map(m)

result = seeds[0][0]
for seed in seeds:
    result = min(result, seed[0])

submit(result, day=day, year=2023)