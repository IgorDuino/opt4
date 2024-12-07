
import math

def f(x):
    return (x - 2)**2 + 3

def golden_section_method(a, b, epsilon):
    golden_ratio = (1 + math.sqrt(5)) / 2  # Golden ratio
    # Initial points
    x1 = b - (b - a) / golden_ratio
    x2 = a + (b - a) / golden_ratio

    while b - a > epsilon:
        f1 = f(x1)
        f2 = f(x2)
        
        if f1 < f2:
            b = x2
        else:
            a = x1
        
        # new points
        x1 = b - (b - a) / golden_ratio
        x2 = a + (b - a) / golden_ratio

    xmin = (a + b) / 2
    return xmin, f(xmin)

a = float(input("Enter the start of the interval a: "))
b = float(input("Enter the end of the interval b: "))
epsilon = float(input("Enter the tolerance epsilon: "))

xmin, fmin = golden_section_method(a, b, epsilon)

print(f"Approximate minimum x_min = {xmin}")
print(f"Function value at the minimum f(x_min) = {fmin}")
