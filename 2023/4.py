from aocd import get_data, submit
import re

day = 4
data = get_data(day=day, year=2023).splitlines()

### PART 1 ###
# result = 0
# for l in data:
#     winning_numbers = [int(n) for n in re.findall(r"(\d+)", re.search(r": ([\d ]*) [|]", l).group(1))]
#     my_numbers = [int(n) for n in re.findall(r"(\d+)", re.search(r"[|] ([\d ]*)$", l).group(1))]

#     points = 0
#     for number in my_numbers:
#         if number in winning_numbers:
#             points = 1 if points == 0 else points * 2
    
#     result += points


### PART 2 ###
card_copies = [1 for _ in range(len(data))]
for i in range(len(data)):
    winning_numbers = [int(n) for n in re.findall(r"(\d+)", re.search(r": ([\d ]*) [|]", data[i]).group(1))]
    my_numbers = [int(n) for n in re.findall(r"(\d+)", re.search(r"[|] ([\d ]*)$", data[i]).group(1))]

    index = 1
    for number in my_numbers:
        if number in winning_numbers and i < len(data) - 1:
            card_copies[i+index] += card_copies[i]
            index += 1


submit(sum(card_copies), day=day, year=2023)