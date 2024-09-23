# task 13
while True:
    
    name= input("Введіть своє ім'я: ")
    surname= input("Введіть своє прізвище: ")
    phone= input("Введіть свій номер телефону: ")

    if name and surname and phone:
        print("Спасибі!")
        break
    else:
        print("Всі поля повинні бути заповненими!")