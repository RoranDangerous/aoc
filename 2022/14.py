from aocd import get_data, submit

day = 14
data = get_data(day=day, year=2022).splitlines()

map = [['.' for _ in range(1000)] for _ in range(1000)]
bottom = 0

# rocks
for l in data:
	coords = l.split(' -> ')
	prev = None
	for coord in coords:
		x, y = [int(c) for c in coord.split(',')]

		if prev == None:
			prev = (x, y)
			continue

		while prev[0] != x or prev[1] != y:
			map[prev[0]][prev[1]] = '#'
			new_x = ((x - prev[0]) // abs(x - prev[0])) if x != prev[0] else 0
			new_y = ((y - prev[1]) // abs(y - prev[1])) if y != prev[1] else 0
			prev = (prev[0]+new_x, prev[1]+new_y)
		
		if prev[1] > bottom:
			bottom = prev[1] + 2

		map[prev[0]][prev[1]] = '#'

# fill bottom
for i in range(len(map)):
	map[i][bottom] = '#'

# sand
def fill_sand():
	count = 0
	while True:
		sand = (500, 0)
		while True:
			# if sand[1] == bottom:
			# 	return count
			if map[sand[0]][sand[1]] == 'o':
				return count

			if map[sand[0]][sand[1]+1] == '.':
				sand = (sand[0], sand[1]+1)
				continue

			if map[sand[0]-1][sand[1]+1] == '.':
				sand = (sand[0]-1, sand[1]+1)
				continue

			if map[sand[0]+1][sand[1]+1] == '.':
				sand = (sand[0]+1, sand[1]+1)
				continue

			map[sand[0]][sand[1]] = 'o'
			count += 1
			break

result = fill_sand()

submit(result, day=day, year=2022)