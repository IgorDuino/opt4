
def f(x):
    return -x**2 + 4*x + 1

# derivative 
def df(x):
    return -2*x + 4

def gradient_ascent(x0, alpha, N):
    x = x0
    for _ in range(N):
        # upd x using gaf
        x = x + alpha * df(x)
    return x, f(x)

x0 = float(input("Enter initial guess x0: "))
alpha = float(input("Enter learning rate alpha: "))
N = int(input("Enter number of iterations N: "))

x_max, f_max = gradient_ascent(x0, alpha, N)

print(f"Approximate maximum x_max = {x_max}")
print(f"Function value at the maximum f(x_max) = {f_max}")

