nota = int(input("Introduce nota: "))

if nota < 0 or nota > 10:
    print("La nota es invalida")
elif nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
elif nota < 10:
    print("Sobresaliente")

print("Version con match: ")
match nota:
    case 0 | 1 | 2 | 3 | 4 |5 :
        print("Suspenso")
    case 5 | 6:
        print("Aprobado")
    case 7 | 8:
        print("Notable")
    case 9 | 10:
        print("Sobresaliente")