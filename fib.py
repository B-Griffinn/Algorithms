# Fibonacci Sequence [0, 1, 1, 2, 3, 5, 8, 13]

# NAIVE APPROACH
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# print(fib(0))

######################
# WITH CACHE

cache = {}

def new_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        value = new_fib(n - 1) + new_fib(n - 2)
        cache[n] = value
        return value

print(new_fib(900))