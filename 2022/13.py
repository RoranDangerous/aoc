from aocd import get_data, submit
from functools import cmp_to_key

day = 13
data = get_data(day=day, year=2022).replace('\n\n', '\n').splitlines()
data.append('[[2]]')
data.append('[[6]]')

def convert(packet):
	lists = []

	number = ''
	for c in packet:
		if c.isnumeric():
			number += c
			continue

		if c == '[':
			lists.append([])
		if c == ']':
			if number:
				lists[-1].append(int(number))

			if len(lists) == 1:
				return lists[0]
			else:
				lists[-2].append(lists[-1])
				lists = lists[:-1]
		
		if c == ',':
			if number:
				lists[-1].append(int(number))

		number = ''


def compare(p1, p2):
	if type(p1) == int and type(p2) == int:
		if p1 == p2:
			return
		if p1 < p2:
			return True
		if p1 > p2:
			return False

	if type(p1) == list and type(p2) == list:
		for i in range(max(len(p1), len(p2))):
			if i >= len(p1):
				return True
			if i >= len(p2):
				return False

			comp = compare(p1[i], p2[i])

			if comp is None:
				continue
			return comp
		return

	if type(p1) == int:
		return compare([p1], p2)

	return compare(p1, [p2])

packets = [convert(p) for p in data]
packets.sort(key=cmp_to_key(lambda x,y: -1 if compare(x,y) in [True, None] else 1))

# result = 0
# for i, pair in enumerate(data):
# 	packet1, packet2 = [convert(p) for p in pair.splitlines()]

# 	if compare(packet1, packet2) in [True, None]:
# 		result += i + 1

result = 1
for i, packet in enumerate(packets):
	if packet in [[[2]], [[6]]]:
		result *= (i+1)

submit(result, day=day, year=2022)