import numpy as np

def func(x):
    return x**2 - np.sin(2*x)


def dfunc(x):
    return 2 * x - 2 * np.cos(2 * x)


def ddfunc(x):
    return 2 + 4 * np.sin(2 * x)


def fibonacci_numbers(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    f1 = 1
    f2 = 1
    for i in range(2, n+1):
        fib = f1 + f2
        f1 = f2
        f2 = fib
    
    return fib


def newton_raphson(x0, f, df, ddf, tol, max_iter=100):
    x_curr = x0
    it = 0

    while it < max_iter:
        x_next = x_curr - df(x_curr) / ddf(x_curr)
        if abs(x_next - x_curr) < tol:
            break
        x_curr = x_next
        it += 1

    x_opt = x_curr
    f_opt = f(x_opt)

    return x_opt, f_opt, it


def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    x_prev = x0
    x_curr = x1
    for i in range(max_iter):
        df_curr = dfunc(x_curr)
        df_prev = dfunc(x_prev)
        if df_curr == df_prev:
            print("Deljenje sa nulom, prekidamo iteraciju.")
            break
        x_next = x_curr - df_curr * (x_curr - x_prev) / (df_curr - df_prev)
        if abs(x_next - x_curr) < tol:
            break
        x_prev, x_curr = x_curr, x_next
    return x_curr, func(x_curr), i


def fibonacci_search(a, b, epsilon):
    n = 1
    while (b - a) / epsilon > fibonacci_numbers(n):
        n += 1

    x1 = a + fibonacci_numbers(n-2)/fibonacci_numbers(n)*(b-a)
    x2 = a + b - x1

    for i in range(2, n+1):
        if func(x1) <= func(x2):
            b = x2
            x1 = a + fibonacci_numbers(n-2)/fibonacci_numbers(n)*(b-a)
            x2 = a + b - x1
        else:
            a = x1
            x1 = a + fibonacci_numbers(n-2)/fibonacci_numbers(n)*(b-a)
            x2 = a + b - x1

    if func(x1) < func(x2):
        x_opt = x1
        f_opt = func(x_opt)
    else:
        x_opt = x2
        f_opt = func(x_opt)

    return x_opt, f_opt, n


def golden_search(a, b, epsilon):
    c = 0.38196

    x1 = a + c * (b - a)
    x2 = a + b - x1

    iter = 0

    while (b - a) > epsilon:
        iter += 1
        if func(x1) <= func(x2):
            b = x2
            x1 = a + c * (b - a)
            x2 = a + b - x1
        else:
            a = x1
            x1 = a + c * (b - a)
            x2 = a + b - x1

    if func(x1) < func(x2):
        x_opt = x1
        f_opt = func(x_opt)
    else:
        x_opt = x2
        f_opt = func(x_opt)

    return x_opt, f_opt, iter


def func2(x):
    return x[0]**2 + x[1]**2


def grad_func(x):
    x = np.array(x).reshape(np.size(x))
    return np.asarray([[2*x[0]], [2*x[1]]])


def steepest_descent(graf, x0, gamma, epsilon, N):
    x = np.array(x0).reshape(len(x0), 1)
    for k in range(N):
        g = graf(x)
        x = x - gamma*g
        if np.linalg.norm(g) < epsilon:
            break
    return x


def steepest_momentum(gradf, x0, gamma, epsilon, omega, N):
    x = np.array(x0).reshape(len(x0), 1)
    v = 0

    for i in range(N):
        g = gradf(x)
        v = omega * v + gamma * g
        x = x - v
        if np.linalg.norm(g) < epsilon:
            break

    return x


def adagrad(gradf, x0, gamma, epsilon1, epsilon, it):
    x = np.array(x0).reshape(len(x0), 1)
    G = np.zeros(shape=x.shape)

    for k in range(it):
        g = gradf(x)
        G = G + np.multiply(g, g)
        x = x - gamma * np.ones(shape=G.shape) / np.sqrt(G+epsilon1) * g
        if (np.linalg.norm(g)) < epsilon:
            break

    return x


def adam(gradf, x0, gamma, omega1, omega2, epsilon1, epsilon, N):
    x = np.array(x0).reshape(len(x0), 1)
    v = 1
    m = 1

    for i in range(N):
        g = gradf(x)
        m = omega1 * m + (1 - omega1) * g
        v = omega2 * v + (1 - omega2) * np.multiply(g, g)
        m_hat = m / (1 - omega1)
        v_hat = np.abs(v / (1 - omega2))
        x = x - gamma * m_hat / np.sqrt(v_hat + epsilon1)
        if np.linalg.norm(g) < epsilon:
            break

    return x


if __name__ == '__main__':
    opt = adam(grad_func, [-1, 1], 0.1, 0.1, 0.9, 1e-8, 1e-4, 100)
    print(opt, func2(opt))