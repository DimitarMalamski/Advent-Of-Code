numbers = []
count = 0

def is_safe_level(numbers):
   if is_ascending(numbers):
      for i in range(1, len(numbers)):
            if int(numbers[i]) - int(numbers[i - 1]) > 3 or int(numbers[i]) - int(numbers[i - 1]) < 1:
               return False        
      return True
   
   elif is_descending(numbers):
      for i in range(1, len(numbers)):
            if int(numbers[i - 1]) - int(numbers[i]) > 3 or int(numbers[i - 1]) - int(numbers[i]) < 1:
               return False       
      return True
   
   return False

def is_descending(numbers):
   for i in range(1, len(numbers)):
         if int(numbers[i - 1]) <= int(numbers[i]):
            return False
   return True


def is_ascending(numbers):
   for i in range(1, len(numbers)):
         if int(numbers[i - 1]) >= int(numbers[i]):
            return False
   return True

with open('2024/Day 2 - Red-Nosed Reports/Part One/input.txt', 'r') as file:
   for line in file:
      splited = line.strip().split(" ")
      if is_safe_level(splited):
         count += 1
      else:
         array = []

         for i in range(len(splited)):
            for j in range(len(splited)):
               if i != j:
                  array.append(splited[j])
            if is_safe_level(array):
               count += 1
               break

            array = []

print(count)

