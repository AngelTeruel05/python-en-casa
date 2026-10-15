lluvia = float(input("Introduce la cantidad de milímetros: "))

if lluvia >= 120:
    print("Alerta Roja")
elif lluvia >= 60:
    print("Alerta Amarilla")
else:
    print("No hay alerta")

match lluvia:
    case m if m >= 120:
        print("Alerta Roja")
    case m if m >= 60:
        print("Alerta Amarilla")
    case _:
        print("No hay alerta")