from aocd import get_data, submit

day = 8
data = get_data(day=day, year=2022).splitlines()

def part1():
	forest = []
	visible = []
	for l in data:
		forest.append(list(l))
		visible.append([False for _ in l])

	# rows
	for i in range(len(forest)):
		highest = '-'
		for j in range(len(forest[i])):
			if forest[i][j] > highest:
				visible[i][j] = True
				highest = forest[i][j]
		
		highest = '-'
		for j in range(len(forest[i])-1, -1, -1):
			if forest[i][j] > highest:
				visible[i][j] = True
				highest = forest[i][j]

	# cols
	for j in range(len(forest[0])):
		highest = '-'
		for i in range(len(forest)):
			if forest[i][j] > highest:
				visible[i][j] = True
				highest = forest[i][j]

		highest = '-'
		for i in range(len(forest)-1, -1, -1):
			if forest[i][j] > highest:
				visible[i][j] = True
				highest = forest[i][j]

	return sum([sum(row) for row in visible])


def part2():
	forest = []
	for l in data:
		forest.append(list(l))

	def get_score(i, j):
		score = 1

		# up
		count = 0
		for ii in range(i-1, -1, -1):
			count += 1
			if forest[ii][j] >= forest[i][j]:
					break

		score *= count

		# down
		count = 0
		for ii in range(i+1, len(forest)):
			count += 1
			if forest[ii][j] >= forest[i][j]:
					break

		score *= count

		# left
		count = 0
		for jj in range(j-1, -1, -1):
			count += 1
			if forest[i][jj] >= forest[i][j]:
					break

		score *= count

		# left
		count = 0
		for jj in range(j+1, len(forest[i])):
			count += 1
			if forest[i][jj] >= forest[i][j]:
					break

		score *= count

		return score

	max_score = 0
	for i in range(len(forest)):
		for j in range(len(forest[0])):
			s = get_score(i, j)
			if s > max_score:
				print(i, j, s)
				max_score = s
	return max_score

result = part2()

submit(result, day=day, year=2022)