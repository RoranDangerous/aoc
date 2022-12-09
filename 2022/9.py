from aocd import get_data, submit

day = 9
data = get_data(day=day, year=2022).splitlines()

# grid_size = 1000
# grid = [[False for _ in range(grid_size)] for _ in range(grid_size)]
# head = [500, 500]
# tail = [500, 500]
# grid[500][500] = True

# def up():
# 	global head, tail, grid
# 	head = [head[0], head[1]-1]
# 	if should_move_tail():
# 		tail = [head[0], head[1]+1]
# 	grid[tail[0]][tail[1]] = True

# def down():
# 	global head, tail, grid
# 	head = [head[0], head[1]+1]
# 	if should_move_tail():
# 		tail = [head[0], head[1]-1]
# 	grid[tail[0]][tail[1]] = True

# def left():
# 	global head, tail, grid
# 	head = [head[0]-1, head[1]]
# 	if should_move_tail():
# 		tail = [head[0]+1, head[1]]
# 	grid[tail[0]][tail[1]] = True

# def right():
# 	global head, tail, grid
# 	head = [head[0]+1, head[1]]
# 	if should_move_tail():
# 		tail = [head[0]-1, head[1]]
# 	grid[tail[0]][tail[1]] = True

# def should_move_tail():
# 	global head, tail, grid
# 	return abs(head[0] - tail[0]) >= 2 or abs(head[1] - tail[1]) >= 2

# for l in data:
# 	directon, steps = l.split(' ')
# 	for i in range(int(steps)):
# 		if directon == 'U':
# 			up()
# 		elif directon == 'D':
# 			down()
# 		elif directon == 'L':
# 			left()
# 		elif directon == 'R':
# 			right()

# result = sum([sum(row) for row in grid])
# submit(result, day=day, year=2022)


grid_size = 1000
grid = [[False for _ in range(grid_size)] for _ in range(grid_size)]
head = [500, 500]
tails = [[500, 500] for _ in range(9)]
grid[500][500] = True

def up():
	head[0] -= 1
	move_tails()

def down():
	head[0] += 1
	move_tails()

def left():
	head[1] -= 1
	move_tails()

def right():
	head[1] += 1
	move_tails()

def move_tails():
	prev = head
	for i in range(len(tails)):
		check_disconnected(tails[i], prev)
		prev = tails[i]
		if i == len(tails) - 1:
			grid[tails[i][0]][tails[i][1]] = True

def check_disconnected(a, b):
	if abs(a[0] - b[0]) >= 2 or abs(a[1] - b[1]) >= 2:
		if b[0] > a[0]:
			a[0] += 1
		elif b[0] < a[0]:
			a[0] -= 1
		
		if b[1] > a[1]:
			a[1] += 1
		elif b[1] < a[1]:
			a[1] -= 1

def debug():
	grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
	for i in range(len(tails)-1, -1, -1):
		grid[tails[i][0]][tails[i][1]] = f'{i+1}'
	grid[head[0]][head[1]] = 'H'

	print('\n'.join([' '.join(row) for row in grid]) + '\n')

for l in data:
	directon, steps = l.split(' ')
	for i in range(int(steps)):
		if directon == 'U':
			up()
		elif directon == 'D':
			down()
		elif directon == 'L':
			left()
		elif directon == 'R':
			right()

		# debug()

result = sum([sum(row) for row in grid])

submit(result, day=day, year=2022)