import re

regex = r"mul\((\d+),(\d+)\)|(don't)\(\)|(do)\(\)"

res = 0
end = True

with open('2024/Day 3 - Mull It Over/Part Two/input.txt', 'r') as file:
   for line in file:
      matches = re.findall(regex, line)

      for match in matches:
         if match[2] == "don't":
            end = False
            continue

         elif match[3] == 'do':
            end = True
            continue
         
         if end:
            res += int(match[0]) * int(match[1])

print(res)