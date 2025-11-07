def func(x):
    f = -1*(x**4-5*x**3-2*x**2+24*x)
    return f


def fibonaci_broj(n):
    if n == 1 or n == 2:
        f = 1
    else:
        fp = 1
        fpp = 1
        for i in range(3, n+1):
            f = fp + fpp
            fpp = fp
            fp = f
    return f


def fibonaci(a, b, tol):
    n = 1
    while ((b-a)/tol) > fibonaci_broj(n):
        n += 1

    x1 = a + fibonaci_broj(n-2)/fibonaci_broj(n)*(b-a)
    x2 = a + b - x1

    for i in range(2, n+1):
        if func(x1) <= func(x2):
            b = x2
            x2 = x1
            x1 = a + b - x2
        else:
            a = x1
            x1 = x2
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
    xopt, fopt, n = fibonaci(a,b,tol)
    print(xopt, fopt, n)
