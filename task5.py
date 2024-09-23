# task 5

a=int(input("Введіть перше число: "))
b=int(input("Введіть друге число: "))
c=int(input("Введіть третє число: "))

if a<b<c:
    print("True")
else: 
    print("False")

if a>0 or b>0 or c>0:
    print("One of the numbers are bigger than zero")
else:
    print("All numbers are negative")

if (a>0)+(b>0)+(c>0) == 1:
    print("Only one number equals 1")
else:
    print("Two or more numbers are bigger than 1 or all numbers are negative")

