#task 7
import math
 
x1=int(input("Введіть першу координату x1: "))
y1=int(input("Введіть другу координату y1: "))
x2=int(input("Введіть третю координату x2: "))
y2=int(input("Введіть четверту координату y2: "))

# queen is walking ONLY diagonally (y1=y2), vertically (x1=x2) or horizontally (x2-x1==y2-y1)

if y1==y2 or x1==x2 or (abs(x2-x1)==abs(y2-y1)):
    print("Queen can walk like that")
else:
    print("Queen can not walk like that")
    