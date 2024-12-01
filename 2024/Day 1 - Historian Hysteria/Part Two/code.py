list_one = []
list_two = []

with open('Day 1 - Historian Hysteria/Part Two/input.txt', 'r') as file:
   for line in file:
      splited = line.strip().split("   ")
      list_one.append(int(splited[0]))
      list_two.append(int(splited[1]))

distance = 0

for i in range(len(list_one)):
   number_one = list_one[i]

   distance += (number_one * list_two.count(number_one))

print(distance)

