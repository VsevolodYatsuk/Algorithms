def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    test_cases = [5, 10, 3, 0]
    for n in test_cases:
        result = factorial(n)
        print(f"Факториал числа {n} равен {result}")