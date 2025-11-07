import numpy as np

def funkcija(x):
    return 5 / 4 * (x[0]**2) + 2 * (x[1] ** 2) + x[0] * x[1]


def gradijent(x):
    x = np.array(x).reshape(np.size(x))
    return np.asarray([[5 / 2 * x[0] + x[1]], [4 * x[1]] + x[0]])


def adagrad(gradf, x0, gamma, epsilon1, epsilon, N):
    x = np.array(x0).reshape(len(x0), 1)
    v = 0
    G = 0
    for k in range(N):
        g = gradf(x)
        G = G + np.multiply(g, g)
        v = (gamma * g)/np.sqrt(G + epsilon1)
        x = x - v
        if np.linalg.norm(g) < epsilon:
            break
    return x


if __name__ == "__main__":
    optimum = adagrad(gradijent, x0=[-1, -1], gamma=0.1, epsilon1=1e-8, epsilon=1e-4, N=100)
    vrednost_funkcije = funkcija(optimum)
    print("Optimum funkcije se nalazi u tacki",optimum,",vrednost funkcije u toj tacki iznosi ", vrednost_funkcije)