

correcta = False

while correcta == False:
    contrasena = input("Introduce la contraseña: ")
    if contrasena == "12345":
        correcta = True
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta, vuelve a intentarlo")