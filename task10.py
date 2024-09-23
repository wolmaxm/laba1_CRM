# task 10
array = list(map(int, input("Введіть елементи масиву через пробіл: ").split()))
average = sum(array) / len(array)

for k in range(len(array)):
    if array[k] > average:
        array[k] -= 18
    
    print(average, array)