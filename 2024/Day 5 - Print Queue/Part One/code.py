lines = [line.strip() for line in open("2024/Day 4 - Ceres Search/Part One/input.txt").readlines()]

adj = {}
inst = []

second_phase = False

for line in lines:
   if line == '\n':
      second_phase = True
      continue

   if not second_phase:
      sp = line.find('|')
      int1 = int(line[:sp - 1])
      int2 = int(line[sp + 1:len(line) - 1])
