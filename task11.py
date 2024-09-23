# task 11
def is_prime(N):
    
    if N <= 1:
        return False
    
    for i in range(2, N):
        if N % i == 0:
            return False  
    return True  


N = int(input("Введіть ціле число N (N > 1): "))

if is_prime(N):
    print("TRUE")
else:
    print("FALSE")
