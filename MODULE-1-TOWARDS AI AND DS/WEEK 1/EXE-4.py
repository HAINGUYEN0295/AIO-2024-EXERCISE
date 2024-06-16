import math
def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result
def approx_sin(x, n):

    if not (x >= 0 and x <= math.pi):
        return print(f'x is not radian')

    if n <= 0:
        return print(f'n is not positive integer')

    result = 0

    for i in range(n + 1):
        result += (-1) ** i * (x ** (2 * i + 1)) / factorial(2 * i + 1)

    return result
def approx_cos(x, n):

    if not (x >= 0 and x <= math.pi):
        return print(f'x is not radian')

    if n <= 0:
        return print(f'n is not positive integer')

    result = 0

    for i in range(n + 1):
        result += (-1) ** i * (x ** (2 * i)) / factorial(2 * i)

    return result
def approx_sinh(x, n):

    if not (x >= 0 and x <= math.pi):
        return print(f'x is not radian')

    if n <= 0:
        return print(f'n is not positive integer')

    result = 0

    for i in range(n + 1):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)

    return result
def approx_cosh(x, n):

    if not (x >= 0 and x <= math.pi):
        return print(f'x is not radian')

    if n <= 0:
        return print(f'n is not positive integer')

    result = 0

    for i in range(n + 1):
        result += (x ** (2 * i)) / factorial(2 * i)

    return result

print(approx_sin(x=3.14, n=10))
print(approx_cos(x=3.14, n=10))
print(approx_sinh(x=3.14, n=10))
print(approx_cosh(x=3.14, n=10))