from aocd import get_data, submit

day = 1
data = get_data(day=day, year=2022).splitlines()
answer = 0

elves = []
current = 0
for l in data:
	print(l)
	if l == "":
		elves.append(current)
		current = 0
		continue

	current += int(l)

elves.sort()


submit(sum(elves[-3:]), day=day, year=2022)