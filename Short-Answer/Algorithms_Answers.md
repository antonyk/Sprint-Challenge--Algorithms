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

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

----
what is f such that
n = dropped + broken

I don't understand what the input and output of this function is supposed to be...

20 dropped + broken
=> 0 broken?

def find_floor(n):

  
  dropped - broken


  return f






