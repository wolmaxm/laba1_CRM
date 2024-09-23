# task 14
for counter in range(10):
    num=int(input(f"Спроба {counter}: Введіть число: "))
    
    if num == 5:
        print("Ви вгадали!")
        break
    else:
        print("Не вгадали :(")
else:
    print("Всі спроби вичерпано!")