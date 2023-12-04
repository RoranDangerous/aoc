import math as m, re
from aocd import get_data, submit

day = 3
board = get_data(day=day, year=2023).splitlines()
# board = '''467..114..
#  ...*......
#  ..35..633.
#  ......#...
#  617*......
#  .....+.58.
#  ..592.....
#  ......755.
#  ...$.*....
#  .664.598..'''.splitlines()

chars = {(r, c): [] for r in range(len(board)) for c in range(len(board))
                    if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(chars)
print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))