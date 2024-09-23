# task 8

A=int(input("Введіть число А: "))
B=int(input("Введіть число В: "))
if A<B:
    
    for k in range(A,B + 1):
     print(k)
     
# amount of numbers
    N=(B-A + 1)
    print(f"Amount of numbers is:{N}")
    
else:
    for l in range(B,A +1):
        print(l)
        
    O=(A-B + 1)
    print(f"Amount of numbers is:{O}")

