while True:
    
    name= input("Введіть своє ім'я: ")
    surname= input("Введіть своє прізвище: ")
    phone= input("Введіть свій номер телефону: ")

    if name or surname or phone:
        print("Спасибі!")
        break
    else:
        print("Заповніть хочаб одне поле!")
        