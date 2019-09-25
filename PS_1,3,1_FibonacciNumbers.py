# Write de definition of a Python procedure fib,
# such that fib(n) return the nth Fibonacci number.

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(10))
print(fib(11))
print(fib(12))
