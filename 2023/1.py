from aocd import get_data, submit

day = 1
data = get_data(day=day, year=2023).splitlines()

### PART 1 ###
# result = 0
# for l in data:
#     for c in l:
#         try:
#             result += int(c) * 10
#             break
#         except ValueError:
#             pass
    
#     for c in reversed(l):
#         try:
#             result += int(c)
#             break
#         except ValueError:
#             pass

### PART 2 ###
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
result = 0
for l in data:
    t = 0
    for i in range(len(l)):
        found = False
        for j in range(len(numbers)):
            if l[i:].startswith(numbers[j]):
                result += (j+1) * 10
                t += (j+1) * 10
                found = True
                break
        
        if found:
            break
        
        try:
            result += int(l[i]) * 10
            t += int(l[i]) * 10
            break
        except ValueError:
            pass

    for i in range(len(l)-1, -1, -1):
        found = False
        for j in range(len(numbers)):
            if l[:i+1].endswith(numbers[j]):
                result += (j+1)
                t += (j+1)
                found = True
                break
        
        if found:
            break
        
        try:
            result += int(l[i])
            t += int(l[i])
            break
        except ValueError:
            pass

submit(result, day=day, year=2023)