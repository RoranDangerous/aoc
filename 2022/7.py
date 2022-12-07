from aocd import get_data, submit

day = 7
data = get_data(day=day, year=2022).splitlines()

class Directory:
	def __init__(self, name, parent=None):
		self.size = 0
		self.name = name
		self.fs = {}
		self.parent = parent


class File:
	def __init__(self, name, size):
		self.name = name
		self.size = size


root = Directory('/')
current_dir = root

for l in data[1:]:
	if l == '$ ls':
		continue

	if l[0:4] == '$ cd':
		direction = l.split(' ')[-1]
		if direction == '..':
			current_dir = current_dir.parent
		else:
			current_dir = current_dir.fs[direction]
		continue

	words = l.split(' ')
	if words[0] == 'dir':
		current_dir.fs[words[1]] = Directory(name=words[1], parent=current_dir)
	else:
		current_dir.fs[words[1]] = File(name=words[1], size=int(words[0]))

# result = 0
def get_size(node):
	if type(node) == File:
		return node.size

	for n in node.fs:
		node.size += get_size(node.fs[n])

	# if node.size <= 100000:
	# 	global result
	# 	result += node.size

	return node.size

get_size(root)


space_needed = 30000000 - 70000000 + root.size
result = 999999999
def find_directory(node):
	if type(node) == File:
		return 999999999

	global result
	if node.size >= space_needed and node.size < result:
		result = node.size
	
	for n in node.fs:
		find_directory(node.fs[n])

find_directory(root)

submit(result, day=day, year=2022)