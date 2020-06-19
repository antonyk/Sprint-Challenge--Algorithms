#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
  a = 0
  while (a < n * n * n):
    a = a + n * n
```
a increments at a rate of n^2 up to n^3
therefore, the loop has roughly O(n) run time

b)
```python
  sum = 0
  for i in range(n):
    j = 1
    while j < n:
      j *= 2
      sum += 1
```
j's loop decrements at a rate of log(j), its scope being cut in half each time
therefore, the total runtime is O(n log n)


c)
```python
  def bunnyEars(bunnies):
    if bunnies == 0:
      return 0

    return 2 + bunnyEars(bunnies-1)
```
runtime is O(n) because of the linear (-1 at reach recursion) progression


## Exercise II


