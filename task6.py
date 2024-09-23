# task 6
x=int(input("Введіть першу координату х (1-8): "))
y=int(input("Введіть другу координату y (1-8): "))

# the field is white, if sum of coordinates will be odd
if (x+y) % 2==0:
    print("Field with that coordinates is black")
else:
    print("Field with what coordinates is white")