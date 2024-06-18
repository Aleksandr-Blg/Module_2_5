def factorial(x):
    if x==1:
        return 1
    return x * factorial(x-1)

print(factorial(5))


# 1 1 2 3 5 8 13 21 44

def fib(x):
    if x in (1, 2):
        return 1
    return fib(x-1)+fib(x-2)

print(fib(10))



