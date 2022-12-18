from aocd import get_data, submit

day = 12
data = get_data(day=day, year=2022).splitlines()

map = [[c for c in row] for row in data]
scores = [[999 for _ in row] for row in data]

S = None
E = None
for i, mr in enumerate(map):
	for j, mc in enumerate(mr):
		if mc == 'S':
			S = (i, j)
			map[i][j] = 'a'
		if mc == 'E':
			E = (i, j)
			map[i][j] = 'z'


def part1():
	cells = { S: 0 }

	def add_cell(i, j, score):
		if (i,j) not in cells:
			cells[(i,j)] = score
			return
		
		cells[(i,j)] = min(cells[(i,j)], score)

	while len(cells.keys()) > 0:
		cell = list(cells.keys())[0]
		cell_score = cells[cell]
		i, j = cell

		del cells[cell]

		if scores[cell[0]][cell[1]] <= cell_score:
			continue

		scores[cell[0]][cell[1]] = cell_score

		# down
		if i < len(map) - 1 and ord(map[i+1][j]) - ord(map[i][j]) <= 1:
			add_cell(i+1, j, cell_score+1)
		
		# up
		if i > 0 and ord(map[i-1][j]) - ord(map[i][j]) <= 1:
			add_cell(i-1, j, cell_score+1)
		
		# left
		if j > 0 and ord(map[i][j-1]) - ord(map[i][j]) <= 1:
			add_cell(i, j-1, cell_score+1)
		
		# right
		if j < len(map[i]) - 1 and ord(map[i][j+1]) - ord(map[i][j]) <= 1:
			add_cell(i, j+1, cell_score+1)

# part1()
# print(scores[E[0]][E[1]])

def part2():
	cells = { E: 0 }
	min_a = 999

	def add_cell(i, j, score):
		if (i,j) not in cells:
			cells[(i,j)] = score
			return
		
		cells[(i,j)] = min(cells[(i,j)], score)

	while len(cells.keys()) > 0:
		cell = list(cells.keys())[0]
		cell_score = cells[cell]
		i, j = cell

		del cells[cell]

		if scores[cell[0]][cell[1]] <= cell_score:
			continue

		scores[cell[0]][cell[1]] = cell_score

		# down
		if i < len(map) - 1 and ord(map[i][j]) - ord(map[i+1][j]) <= 1:
			add_cell(i+1, j, cell_score+1)
		
		# up
		if i > 0 and ord(map[i][j]) - ord(map[i-1][j]) <= 1:
			add_cell(i-1, j, cell_score+1)
		
		# left
		if j > 0 and ord(map[i][j]) - ord(map[i][j-1]) <= 1:
			add_cell(i, j-1, cell_score+1)
		
		# right
		if j < len(map[i]) - 1 and ord(map[i][j]) - ord(map[i][j+1]) <= 1:
			add_cell(i, j+1, cell_score+1)

		if map[i][j] == 'a' and cell_score < min_a:
			min_a = cell_score

	return min_a

result = part2()
submit(result, day=day, year=2022)