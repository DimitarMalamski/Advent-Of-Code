list_one = []
list_two = []

with open('Day 1 - Historian Hysteria/input.txt', 'r') as file:
   for line in file:
      splited = line.strip().split("   ")
      list_one.append(int(splited[0]))
      list_two.append(int(splited[1]))

distance = 0

for i in range(len(list_one)):
   number_one = min(list_one)
   number_two = min(list_two)

   distance += abs(number_one - number_two)

   list_one.remove(number_one)
   list_two.remove(number_two)

print(distance)

