def fib(n):
    """
    Calculate the nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)