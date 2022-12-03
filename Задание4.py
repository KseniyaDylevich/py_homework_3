def decimal_to_binary (dec):
  bin = ''
  while dec > 0:
    bin += str(dec % 2)
    dec = dec // 2
  return bin

for i in [1, 3, 4, 5, 6, 7, 8, 9, 10, 45]:
  print (decimal_to_binary (i))