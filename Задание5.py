def create_fibonachi_list (number:int):
  fib_1 = 0
  fib_2 = 1
  fib_list_0 = [0] # список, содержащий только ноль
  fib_list_1 = [] # список чисел фибоначи (справа от нуля)
  fib_list_2 = [] # список чисел фибоначи (слева от нуля нуля)

  for i in range(number):
      fib_1, fib_2 = fib_2, fib_1 + fib_2
      fib_list_1.append(fib_1)

  # создадим на основе первого второй список, но с чередующимися знаками, после чего реверсируем его
  for i in range(len(fib_list_1)):
      temp =(fib_list_1[i])
      if i % 2 != 0:
        temp = temp * (-1)
      fib_list_2.append(temp)
  fib_list_2.reverse()

  # объединим все три списка в один 
  return fib_list_2 + fib_list_0 + fib_list_1

print (create_fibonachi_list (5))