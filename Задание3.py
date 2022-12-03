def fractional_diff (list):
  min_fract = max_fract = (float(list[0])*10000)%10000
  for i in list:
    temp = round((float(i)*10000)%10000, 4)
    if  temp < min_fract:
      min_fract = temp
    if  temp > max_fract:
      max_fract = temp
  return (max_fract - min_fract)/10000

my_list = [1.1, 1.2, 3.1, 10.01]

print(fractional_diff (my_list))