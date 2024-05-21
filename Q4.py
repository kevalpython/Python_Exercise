def fibonacci(n,memo={}):
    print(memo)
    if n in memo:
        
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fibonacci(n-1,memo) + fibonacci(n-2,memo)
        return memo[n]

N = 8
result = fibonacci(N)
print("Output:", result)
fib_60 = fibonacci(60)
fib_90 = fibonacci(90)
print("60th Fibonacci term:", fib_60)
print("90th Fibonacci term:", fib_90)