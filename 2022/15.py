import re
from aocd import get_data, submit

day = 15
data = get_data(day=day, year=2022).splitlines()

boundary = 4000000 + 1
map = [[] for _ in range(boundary)]

def add_range(index, r1):
	global map
	new_row = map[index]
	new_row.append(r1)
	new_row.sort(key=lambda x: x[0])

	map[index] = []
	i = 0
	for r in new_row:
		if i == 0:
			i += 1
			map[index].append(r)
			continue
	
		prev = map[index][i-1]
		# merge
		if r[0] <= prev[1]:
			map[index][i-1] = (prev[0], max(prev[1], r[1]))
		else:
			i += 1
			map[index].append(r)


for l in data:
	print(l)
	sensor_coords = re.search("^Sensor at (.*):", l).group(1)
	beacon_coords = re.search("closest beacon is at (.*)$", l).group(1)
	sensor = (
		int(re.search('x=(.*),', sensor_coords).group(1)),
		int(re.search('y=(.*)$', sensor_coords).group(1))
	)
	beacon = (
		int(re.search('x=(.*),', beacon_coords).group(1)),
		int(re.search('y=(.*)$', beacon_coords).group(1))
	)
	distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

	for i in range(max(sensor[1]-distance, 0), min(sensor[1]+distance+1, boundary)):
		x_range = distance - abs(sensor[1] - i)
		x_range = (max(sensor[0]-x_range, 0), min(sensor[0]+x_range+1, boundary))
		
		add_range(i, x_range)


def find():
	for i, row in enumerate(map):
		if row != [(0, 4000001)]:
			return row[1] * 4000000 + i

result = find()

submit(result, day=day, year=2022)