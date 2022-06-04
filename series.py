def fibonacci(n):
    # Integer series starts with 0 and 1
    # the next integer is the summation of the previous two.
   if n == 0 or n == 1:
       return n
   else:
       return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    # Integer series starts with 2 and 1
    # the next integer is the summation of the previous two.
   if n == 0:
       return 2
   elif n == 1:
     return 1
   else:
       return lucas(n-1) + lucas(n-2)

def sum_series(x, y = 0, z = 1):
    # Integer series starts with x and y, the default value for them
    # is x = 0, y = 1, the next integer is the summation
    # of the previous two.
    if x == 0:
        return y
    elif x == 1:
        return z
    else:
        return sum_series(x - 1, y, z) + sum_series(x - 2, y, z)

