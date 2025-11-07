def find_fibonacci_N(a, b, epsilon):
    target = (b - a) / epsilon  
    F1, F2 = 1, 1 
    N = 2  
    
    while F2 < target: 
        F1, F2 = F2, F1 + F2 
        N += 1 
    
    return N 


if __name__ == "__main__":
    a = 0
    b = 10
    epsilon = 0.01
    N = find_fibonacci_N(a, b, epsilon)
    print(f"Broj iteracija: {N}")
