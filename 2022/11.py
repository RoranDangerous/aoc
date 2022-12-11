from aocd import submit
from functools import reduce

day = 11

class Monkey:
	def __init__(self, items, operation, test):
		self.items = items
		self.operation = operation
		self.test = test

monkeys = [
	Monkey(
		items=[77, 69, 76, 77, 50, 58],
		operation=lambda x: x * 11,
		test=lambda x: 1 if x % 5 == 0 else 5
	),
	Monkey(
		items=[75, 70, 82, 83, 96, 64, 62],
		operation=lambda x: x + 8,
		test=lambda x: 5 if x % 17 == 0 else 6
	),
	Monkey(
		items=[53],
		operation=lambda x: x * 3,
		test=lambda x: 0 if x % 2 == 0 else 7
	),
	Monkey(
		items=[85, 64, 93, 64, 99],
		operation=lambda x: x + 4,
		test=lambda x: 7 if x % 7 == 0 else 2
	),
	Monkey(
		items=[61, 92, 71],
		operation=lambda x: x * x,
		test=lambda x: 2 if x % 3 == 0 else 3
	),
	Monkey(
		items=[79, 73, 50, 90],
		operation=lambda x: x + 2,
		test=lambda x: 4 if x % 11 == 0 else 6
	),
	Monkey(
		items=[50, 89],
		operation=lambda x: x + 3,
		test=lambda x: 4 if x % 13 == 0 else 3
	),
	Monkey(
		items=[83, 56, 64, 58, 93, 91, 56, 65],
		operation=lambda x: x + 5,
		test=lambda x: 1 if x % 19 == 0 else 0
	),
]

monkey_items = [0 for _ in range(len(monkeys))]

rounds = 10000
for i in range(rounds):
	for i, monkey in enumerate(monkeys):
		for item in monkey.items:
			new_item = monkey.operation(item) % 9699690 #// 3
			monkeys[monkey.test(new_item)].items.append(new_item)

		monkey_items[i] += len(monkey.items)
		monkey.items = []

monkey_items.sort()
result = reduce((lambda x, y: x * y), monkey_items[-2:])

submit(result, day=day, year=2022)