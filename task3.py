# task 3
import math
x1=int(input('Введіть першу координату х1 '))
y1=int(input('Введіть другу координату у1 '))
x2=int(input('Введіть третю координату x2 '))
y2=int(input('Введіть четверту координату y2 '))
p1=abs(x2-x1) #finding the length of side
q=abs(y2-y1) #finding the length of another side
o=p1*q
s1=2*(p1+q)
print(o,s1)