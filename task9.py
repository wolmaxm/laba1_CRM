# task 9

N=int(input("Enter the N number (N>0): "))
if N <= 0:
    print("The N number must be more than 0")
else:
    N=str(N)
    n_rev=N[::-1]
    print(n_rev)
    
