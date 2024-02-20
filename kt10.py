def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    n = 10
    result = fibonacci(n)
    print(f"n-е число в последовательности Фибоначчи для n={n}:", result)