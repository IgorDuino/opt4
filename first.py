def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def bisection_method(a, b, epsilon):
    fa = f(a)
    fb = f(b)
    
    if abs(fa) < epsilon:
        return a
    if abs(fb) < epsilon:
        return b
    
    if fa * fb > 0:
        print("The function must have opposite signs at the endpoints a and b.")
        return None
    
    iterations = 0
    while True:
        c = (a + b) / 2
        fc = f(c)
        
        if abs(fc) < epsilon:
            print(f"Converged after {iterations} iterations")
            return c
            
        iterations += 1
        if fc * fa < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

a = float(input("Enter the start of the interval a: "))
b = float(input("Enter the end of the interval b: "))
epsilon = float(input("Enter the tolerance epsilon: "))

root = bisection_method(a, b, epsilon)

if root is not None:
    print(f"Approximate root: {root}")
    print(f"f(root) = {f(root)}")