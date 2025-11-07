import math

def func(x):
    f = x**4-5*x**3-2*x**2+24*x
    return f


def dfunc(x):
    f = 4*x**3-15*x**2-4*x+24
    return f


def ddfunc(x):
    f = 12*x**2-30*x-4
    return f


'''def njutn_rapson(x0, tol):
    x_novo = x0
    x_pre = math.inf
    iter = 0

    while(abs(x_pre-x_novo)>tol):
        iter += 1
        x_pre = x_novo
        x_novo = x_pre - dfunc(x_pre)/ddfunc(x_pre)

    xopt = x_novo
    fopt = func(xopt)
    return xopt, fopt, iter'''

def njutn_rapsonov_metod(x0, epsilon):
    x_novo = x0
    x_pre = math.inf

    iter = 0
    max_iter = 30

    while abs(x_pre - x_novo) > epsilon:
        iter += 1
        x_pre = x_novo
        x_novo = x_pre - dfunc(x_pre) / ddfunc(x_pre)

        if iter >= max_iter:
            break

    xopt = x_novo
    fopt = func(xopt)
    return xopt, fopt, iter


if __name__ == "__main__":
    '''tol = 0.0001
    init_guess = 1
    [xopt, fopt, iter] = njutn_rapson(init_guess, tol)
    print(xopt, fopt, iter)'''
    x_opt, f_opt, iter = njutn_rapsonov_metod(x0=1, epsilon=0.0001)

    print(f'Stacionarna tačka funkcije f(x) je u {x_opt}, a optimalna vrednost funkcije iznosi {f_opt}. Algoritam je izvršen u {iter} iteracija.')