def fibonacci_generator_n_terms(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence with {n} terms: {list(fibonacci_generator_n_terms(n))}")