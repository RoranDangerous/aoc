from aocd import get_data, submit

day = 2
data = get_data(day=day, year=2022).splitlines()

f = {
	'A': 1,
	'B': 2,
	'C': 3
}

s = {
	'X': 1,
	'Y': 2,
	'Z': 3
}

p = [0, 1, 2, 3]

total = 0
for l in data:
	m = l.split(' ')
	fm = f[m[0]]
	sm = s[m[1]]

	if sm == 1:
		if fm == 1:
			total += 3
		if fm == 2:
			total += 1
		if fm == 3:
			total += 2
	
	if sm == 2:
		total += p[fm] + 3
	
	if sm == 3:
		total += 6
		if fm == 1:
			total += 2
		if fm == 2:
			total += 3
		if fm == 3:
			total += 1


submit(total, day=day, year=2022)