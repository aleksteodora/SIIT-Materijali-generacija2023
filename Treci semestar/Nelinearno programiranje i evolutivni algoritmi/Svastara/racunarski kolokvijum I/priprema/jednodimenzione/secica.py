import math

def func(x):
    f = x**4-5*x**3-2*x**2+24*x
    return f


def dfunc(x):
    f = 4*x**3-15*x**2-4*x+24
    return f


def secica(x1,x0,tol):
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

'''def metod_secice(x1, x0, epsilon):
    x_pre = x0     
    x_novo = x1         

    iter = 0           

    while abs(x_novo - x_pre) > epsilon:  
        iter += 1
        x_ppre = x_pre                          
        x_pre = x_novo                          
        x_novo = x_pre - dfunc(x_pre) * (x_pre - x_ppre) / (dfunc(x_pre) - dfunc(x_ppre))  

    x_opt = x_novo      
    f_opt = func(x_opt) 
    return x_opt, f_opt, iter '''


if __name__ == "__main__":
    tol = 0.0001
    init_guess1 = 0
    init_guess2 = 3
    [xopt,fopt,iter] = secica(init_guess1,init_guess2,tol)
    print(xopt, fopt, iter)

    '''[x_opt, f_opt, iter] = metod_secice(x0=0, x1=3, epsilon=0.0001)

    print(f'Optimum funkcije f(x) je u tački {x_opt} i iznosi {f_opt}. Algoritam je izvršen u {iter} iteracija.')'''