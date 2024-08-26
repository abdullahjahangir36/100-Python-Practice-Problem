# Print the first 20 numbers of a Fibonacci series
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series

# Number of Fibonacci numbers to print
n = 20
# Generate and print the first 20 numbers of the Fibonacci series
fib_numbers = fibonacci_series(n)
print(f"The first {n} numbers of the Fibonacci series are:")
print(fib_numbers)
