from aocd import get_data, submit

day = 3
data = get_data(day=day, year=2022).splitlines()

total = 0
index = 0
d = {}
for l in data:
	# index = int(len(l) / 2)
	# d = {}
	# for i in range(0, index):
	# 	d[l[i]] = True
	
	# for i in range(index, len(l)):
	# 	letter = l[i]
	# 	if letter in d and d[letter]:
	# 		if ord(letter) <= ord('Z'):
	# 			total += ord(letter) - ord('A') + 1 + 26
	# 		else:
	# 			total += ord(letter) - ord('a') + 1
	# 		break
	index += 1
	if index == 1:
		for c in l:
			d[c] = 1
		continue

	if index == 2:
		for c in l:
			if c in d:
				d[c] = 2
		continue

	if index == 3:
		for c in l:
			if c in d and d[c] == 2:
				if ord(c) <= ord('Z'):
					total += ord(c) - ord('A') + 1 + 26
				else:
					total += ord(c) - ord('a') + 1
				break

		d = {}
		index = 0


submit(total, day=day, year=2022)