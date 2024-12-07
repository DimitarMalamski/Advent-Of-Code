lines = [line.strip() for line in open("2024/Day 6 - Guard Gallivant/Part One/input.txt").readlines()]

obs = []
px, py = 0, 0

for i in range(len(lines)):
   for j in range(len(lines[i])):
      if lines[i][j] == '^':
         px, py = i,j
      elif lines[i][j] == '#':
         obs.append((i,j))

visited = set()
visited.add((px,py))

dirs_right = {'up': (0,1), 'right': (1, 0), 'down': (0, -1), 'left': (-1, 0)}
dirs_stright = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
dirs = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}

dir = (-1, 0)

def check(px, py):
   return px >= 0 and py >= 0 and px < len(lines) and len(lines[px])

def calc_dir(dir):
   if dir == (-1, 0):
      return (0, 1)
   elif dir == (0, 1):
      return (1, 0)
   elif dir == (1, 0):
      return (0, -1)
   else:
      return (-1, 0)

while check(px,py):
   next_x, next_y = px + dir[0], py + dir[1]

   if (next_x, next_y) in obs:
      dir = calc_dir(dir)
      px += dir[0]
      py += dir[1]

      if not check(px, py):
         break

      visited.add((px, py))
      continue

   if not check(next_x, next_y):
      visited.add((px, py))
      break

   px, py = next_x, next_y
   visited.add((px, py))

print(len(visited))