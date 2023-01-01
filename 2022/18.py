from aocd import get_data, submit
import numpy as np

day = 18
data = get_data(day=day, year=2022)
data = data.splitlines()

size = 22
lava = [[[None for _ in range(size)] for _ in range(size)] for _ in range(size)]
for l in data:
	x, y, z = map(int, l.split(','))
	lava[x][y][z] = True

lava = np.pad(lava, (1,1))
water = []
for x, xx in enumerate(lava):
	for y, yy in enumerate(xx):
		for z, zz in enumerate(yy):
			if zz == 0:
				water.append((x,y,z))

while len(water) > 0:
	x,y,z = water[0]
	water = [*water[1:]]
	lava[x][y][z] = False

	if x > 0 and lava[x-1][y][z] is None:
		water.append((x-1, y, z))
	if x < len(lava) - 1 and lava[x+1][y][z] is None:
		water.append((x+1, y, z))
	if y > 0 and lava[x][y-1][z] is None:
		water.append((x, y-1, z))
	if y < len(lava[x]) - 1 and lava[x][y+1][z] is None:
		water.append((x, y+1, z))
	if z > 0 and lava[x][y][z-1] is None:
		water.append((x, y, z-1))
	if z < len(lava[x][y]) - 1 and lava[x][y][z+1] is None:
		water.append((x, y, z+1))

result = 0
for x, xx in enumerate(lava):
	for y, yy in enumerate(xx):
		for z, zz in enumerate(yy):
			if not zz:
				continue

			if x == 0 or lava[x-1][y][z] is False:
				result += 1
			if x == len(lava) - 1 or lava[x+1][y][z] is False:
				result += 1
			if y == 0 or lava[x][y-1][z] is False:
				result += 1
			if y == len(lava[x]) - 1 or lava[x][y+1][z] is False:
				result += 1
			if z == 0 or lava[x][y][z-1] is False:
				result += 1
			if z == len(lava[x][y]) - 1 or lava[x][y][z+1] is False:
				result += 1

submit(result, day=day, year=2022)