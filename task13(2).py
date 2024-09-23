while True:
    
    name= input("Введіть своє ім'я: ")
    surname= input("Введіть своє прізвище: ")
    phone= input("Введіть свій номер телефону: ")

    if name and surname:
        print("Спасибі!")
        break
    else:
        print("Не залишайте поля з іменем і прізвищем пусті")