# exercise 4:

def factorial(k):
    if k == 0 or k == 1:
        return 1
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result

def approx_sin(x, n):
    result = 0
    for k in range(n + 1):
        term = ((-1) ** k) * (x ** (2 * k + 1)) / factorial(2 * k + 1)
        result += term
    return result

def approx_cos(x, n):
    result = 0
    for k in range(n + 1):
        term = ((-1) ** k) * (x ** (2 * k)) / factorial(2 * k)
        result += term
    return result

def approx_sinh(x, n):
    result = 0
    for k in range(n + 1):
        term = (x ** (2 * k + 1)) / factorial(2 * k + 1)
        result += term
    return result

def approx_cosh(x, n):
    result = 0
    for k in range(n + 1):
        term = (x ** (2 * k)) / factorial(2 * k)
        result += term
    return result

def exercise4():
  x = float(input("Input x (radian): "))

  n = int(input("Input n (n > 0): "))

  if n <= 0:
    print("n must be greater than 0")
    return

  print(f"approx_sin(x={x}, n={n}) = {approx_sin(x, n)}")
  print(f"approx_cos(x={x}, n={n}) = {approx_cos(x, n)}")
  print(f"approx_sinh(x={x}, n={n}) = {approx_sinh(x, n)}")
  print(f"approx_cosh(x={x}, n={n}) = {approx_cosh(x, n)}")

exercise4()