import re

regex = r"mul\((\d+),(\d+)\)"

res = 0

with open('2024/Day 3 - Mull It Over/Part One/input.txt', 'r') as file:
   for line in file:
      matches = re.findall(regex, line)

      for match in matches:
         res += int(match[0]) * int(match[1])

print(res)