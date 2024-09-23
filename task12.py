# task 12
import math

x=float(input("Введіть число x: "))
y=float(input("Введіть число y: "))
z=float(input("Введіть число z: "))

a=math.atan(z+y)+ math.sqrt(math.pow(z,2)-y)+abs(x)
print(a)