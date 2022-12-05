from aocd import get_data, submit

day = 5
data = get_data(day=day, year=2022).split(' 1   2   3   4   5   6   7   8   9 \n\n')

containers_str = [
	'SZPDLBFC',
	'NVGPHWB',
	'FWBJG',
	'GJNFLWCS',
	'WJLTPMSH',
	'BCWGFS',
	'HTPMQBW',
	'FSWT',
	'NCR',
]

containers = [list(c) for c in containers_str]

for l in data[1].splitlines():
	words = l.split(' ')
	num = int(words[1])
	index_from = int(words[3]) - 1
	index_to = int(words[5]) - 1 
	
	# for i in range(num):
	# 	containers[index_to].append(containers[index_from][-1])
	# 	containers[index_from].pop()

	containers[index_to] += containers[index_from][-num:]
	containers[index_from] = containers[index_from][:-num]

result = ''
for c in containers:
	result += c[-1]
submit(result, day=day, year=2022)