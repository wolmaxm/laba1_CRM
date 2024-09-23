# task 9

N=int(input("Enter the N number (N>0): "))
if N <= 0:
    print("The N number must be more than 0")
else:
    rev_N = 0
    
while N > 0:
    i= N % 10
    rev_N = rev_N * 10 + i
    N = N // 10 
    print(rev_N)