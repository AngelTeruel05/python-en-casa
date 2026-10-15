edad = int(input("Introduce edad: "))

if edad <= 0:
    print("Edad invalida")
elif edad >= 120:
    print("Eres un Vampiro")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
