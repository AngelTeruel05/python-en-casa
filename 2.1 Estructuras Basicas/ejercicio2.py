precio = float(input("Introduce precio del producto: "))
iva = input("Tipo de iVA (general, reducido o superreducido): ")

if iva == "general":
    precio_final = precio * 1.21
elif iva == "reducido":
    precio_final = precio * 1.10
elif iva == "superreducido":
    precio_final = precio * 1.04

match iva:
    case "general":
        precio_final = precio * 1.21
    case "reducido":
        precio_final = precio * 1.10
    case "superreducido":
        precio_final = precio * 1.04

print("El precio final del producto es: ",precio_final)

