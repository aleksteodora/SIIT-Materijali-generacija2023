import math

def func(x):
    f = math.e**(x) + math.cos(3*x)
    return f

def dfunc(x):
    f = math.e**(x) - 3 * (math.sin(3*x))
    return f


def secica(x1, x0, tol):
    x_pre = x0
    x_ppre = math.inf
    x_novo = x1
    iter = 0

    while(abs(x_novo-x_pre)>tol):
        iter += 1
        x_ppre = x_pre
        x_pre = x_novo
        x_novo = x_pre-dfunc(x_pre)*(x_pre-x_ppre)/(dfunc(x_pre)-dfunc(x_ppre))

    xopt = x_novo
    fopt = func(xopt)
    return xopt, fopt, iter


if __name__ == "__main__":
    tol = 0.01
    guess1 = 1.0
    guess2 = 3.0
    [xopt,fopt,iter] = secica(guess1,guess2,tol)
    print(xopt, fopt, iter)