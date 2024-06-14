"""
Fibonacci Series
"""

def fibonacci(n, memo=None):
    """
    This function generates the Fibonacci series up to the Nth term.

    Args:
    n (int): The end term of the Fibonacci series.
        
    Returns:
    int: The Fibonacci series up to the Nth term.
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

N = 8
RESULT = fibonacci(N)
print("Output:", RESULT)
FIB_60 = fibonacci(60)
FIB_90 = fibonacci(90)
print("60th Fibonacci term:", FIB_60)
print("90th Fibonacci term:", FIB_90)
