def mult_pair_list (list):
  result_list = []
  start_index = 0
  end_index = len(list)-1

  while (start_index <= end_index):
    result_list.append(list[start_index]*list[end_index])
    start_index+=1
    end_index-=1

  return result_list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print (mult_pair_list (list))