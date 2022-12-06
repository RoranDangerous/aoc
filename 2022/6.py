from aocd import get_data, submit

day = 6
data = get_data(day=day, year=2022)

result = 0
chars = []
for i in range(len(data)):
	chars.append(data[i])

	# if i < 4:
	# 	continue

	if i < 14:
		continue

	chars = chars[1:]

	if len(set(chars)) == 14:
		result = i + 1
		break

submit(result, day=day, year=2022)