import math

def func(x):
    f = -1*(x**4-5*x**3-2*x**2+24*x)
    return f

def zlatni_presek(a, b, tol):
    c=(3-math.sqrt(5))/2
    x1 = a + c*(b-a)
    x2 = a + b - x1
    n = 1

    while (b-a)>tol:
        n += 1
        if func(x1) <= func(x2):
            b = x2
            x1 = a + c*(b-a)
            x2 = a + b - x1
        else:
            a = x1
            x1 = a + c * (b - a)
            x2 = a + b - x1

    if func(x1) < func(x2):
        xopt = x1
        fopt = func(x1)
    else:
        xopt = x2
        fopt = func(x2)

    return xopt, fopt, n

if __name__ == "__main__":
    a = 0
    b = 3
    tol = 0.0001
    xopt, fopt, n = zlatni_presek(a, b, tol)
    print(xopt, fopt, n)