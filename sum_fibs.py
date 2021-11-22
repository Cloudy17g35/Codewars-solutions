'''Create a function that takes an argument n and sums 
even Fibonacci numbers up to n's index in the Fibonacci sequence.'''


memo = {0:0, 1:1}
def fib(n):
    for _ in range(n):
        if n not in memo:
            memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

def sum_fibs(n:int) -> int:
    return sum([fib(i) for i in range(1, n + 1) if fib(i) % 2 == 0])
