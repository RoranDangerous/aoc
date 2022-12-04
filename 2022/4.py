from aocd import get_data, submit

day = 4
data = get_data(day=day, year=2022).splitlines()

result = 0
for l in data:
	elves = l.split(',')
	elf1 = [int(e) for e in elves[0].split('-')]
	elf2 = [int(e) for e in elves[1].split('-')]

	# if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
	# 	result += 1
	# elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
	# 	result += 1

	if elf1[0] <= elf2[1] and elf1[1] >= elf2[0]:
		result += 1
	elif elf2[0] <= elf1[1] and elf2[1] >= elf1[0]:
		result += 1

submit(result, day=day, year=2022)