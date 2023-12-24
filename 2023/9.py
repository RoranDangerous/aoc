from aocd import get_data, submit

day = 9
data = get_data(day=day, year=2023).splitlines()

### PART 1 ###
# result = 0
# for l in data:
#     row = [int(n) for n in l.split(" ")]
#     value = 0

#     while True:
#         diffs = []
#         for i in range(len(row)-1):
#             diffs.append(row[i+1]-row[i])
        
#         zeroes = True
#         for diff in diffs:
#             if diff != 0:
#                 zeroes = False
#                 break
        
#         value += row[-1]
#         if zeroes:
#             break
        
#         row = diffs
    
#     result += value

### PART 2 ###
result = 0
for l in data:
    row = [int(n) for n in l.split(" ")]
    value = 0
    iterations = 0

    while True:
        iterations += 1
        diffs = []
        value = row[0] - value
        for i in range(len(row)-1):
            diffs.append(row[i+1]-row[i])
        
        zeroes = True
        for diff in diffs:
            if diff != 0:
                zeroes = False
                break

        if zeroes:
            value *= -1 if iterations % 2 == 0 else 1
            break
        
        row = diffs

    result += value

submit(result, day=day, year=2023)