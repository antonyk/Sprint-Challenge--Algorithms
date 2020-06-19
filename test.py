

def myfunc(n):

  sum = 0
  for i in range(n):
    j = 1
    while j < n:
      j *= 2
      sum += 1

  return sum


print(myfunc(1000000))