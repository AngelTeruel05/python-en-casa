print("9. Pedir al usuario un número entero y mostrar por pantalla si el número es primo o no.")

numero = int(input("Introduce un número entero: "))

if numero < 2:
    print("El número no es primo.")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")

