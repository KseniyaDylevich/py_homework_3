def sum_odd (list):
  sum = 0
  for i in range (len(list)):
    if i % 2 != 0:
      sum += list[i]
  return sum
  
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum_odd (my_list))