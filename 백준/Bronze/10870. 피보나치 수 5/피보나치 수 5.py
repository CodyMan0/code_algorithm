# 피보나치 f(n) = f(n-1) + f(n-2)


def fibonacci(n):

    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))