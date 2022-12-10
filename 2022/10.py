from aocd import get_data, submit

day = 10
data = get_data(day=day, year=2022).splitlines()

x = 1
cycle = 0

signal_strength = 0
def check_cycle():
	global signal_strength
	if cycle in [20, 60, 100, 140, 180, 220]:
		signal_strength += x * cycle

img = [[] for _ in range(6)]
def draw():
	index =  (cycle - 1) // 40

	pixel_position = cycle - (index * 40)
	if pixel_position >= x and pixel_position <= (x + 2):
		img[index].append('#')
	else:
		img[index].append('.')


for l in data:
	cycle += 1

	# check_cycle()
	draw()

	if l == 'noop':
		continue

	op, num = l.split(' ')
	cycle += 1

	# check_cycle()
	draw()

	x += int(num)

print('\n'.join([ ''.join(row) for row in img]))
# submit(signal_strength, day=day, year=2022)