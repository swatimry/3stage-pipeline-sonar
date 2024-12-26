def fibonacci(n):
    # Starting values
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Get Fibonacci sequence up to 10 terms
fibonacci(10)
