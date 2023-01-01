from aocd import get_data, submit

day = 17
data = get_data(day=day, year=2022)
movements = list(data)

room = []
height = 0

def trim_room():
	global room

	while room and room[0] == ['.' for _ in range(7)]:
		room = [*room[1:]]

def add_space():
	global room
	trim_room()
	room = [
		['.' for _ in range(7)],
		['.' for _ in range(7)],
		['.' for _ in range(7)],
		*room
	]

def add_rock_1():
	global room
	room = [
		['.', '.', '@', '@', '@', '@', '.'],
		*room
	]

def add_rock_2():
	global room
	room = [
		['.', '.', '.', '@', '.', '.', '.'],
		['.', '.', '@', '@', '@', '.', '.'],
		['.', '.', '.', '@', '.', '.', '.'],
		*room
	]

def add_rock_3():
	global room
	room = [
		['.', '.', '.', '.', '@', '.', '.'],
		['.', '.', '.', '.', '@', '.', '.'],
		['.', '.', '@', '@', '@', '.', '.'],
		*room
	]

def add_rock_4():
	global room
	room = [
		['.', '.', '@', '.', '.', '.', '.'],
		['.', '.', '@', '.', '.', '.', '.'],
		['.', '.', '@', '.', '.', '.', '.'],
		['.', '.', '@', '.', '.', '.', '.'],
		*room
	]

def add_rock_5():
	global room
	room = [
		['.', '.', '@', '@', '.', '.', '.'],
		['.', '.', '@', '@', '.', '.', '.'],
		*room
	]

add_rock = [
	add_rock_1,
	add_rock_2,
	add_rock_3,
	add_rock_4,
	add_rock_5
]

def move_right():
	global room
	for row in room:
		for j, col in enumerate(row):
			if col == '@':
				if j == len(row)-1:
					return
				if row[j+1] == '#':
					return

	for row in room:
		for j in range(len(row)-1, -1, -1):
			if row[j] == '@':
				row[j+1] = '@'
				row[j] = '.'

def move_left():
	global room
	for row in room:
		for j, col in enumerate(row):
			if col == '@':
				if j == 0:
					return
				if row[j-1] == '#':
					return

	for row in room:
		for j, col in enumerate(row):
			if col == '@':
				row[j-1] = '@'
				row[j] = '.'

def move_down():
	global room
	for i, row in enumerate(room):
		for j, col in enumerate(row):
			if col == '@':
				if i == len(room) - 1:
					return False
				if room[i+1][j] == '#':
					return False

	for i in range(len(room)-1, -1, -1):
		for j, col in enumerate(room[i]):
			if col == '@':
				room[i+1][j] = '@'
				room[i][j] = '.'


def convert():
	for i, row in enumerate(room):
		for j, col in enumerate(row):
			if col == '@':
				room[i][j] = '#'

def check_floor():
	global room, height
	for i, row in enumerate(room):
		if row == ['#' for _ in range(7)]:
			height += len(room) - i
			room = room[:i]
			return

def print_room():
	print('\n'.join([''.join(row) for row in room]))

rocks = 0
rock_type = 0
movement_index = 0
while rocks < 2022:
	rocks += 1
	add_space()
	add_rock[rock_type]()
	while True:
		if movements[movement_index % len(movements)] == '>':
			move_right()
		else:
			move_left()
		movement_index += 1
		if move_down() == False:
			convert()
			break
	
	check_floor()
	rock_type += 1
	rock_type %= 5


submit(len(room), day=day, year=2022)