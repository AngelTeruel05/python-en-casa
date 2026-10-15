print("10. Pedir al usuario dos valores enteros y mostrar por pantalla todos los números primos dentro de ese rango. Si el primer número es mayor que el primero se mostrará por pantalla un mensaje de error.")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print("Error: el primer número es mayor que el segundo.")
else:
    print("Los números primos entre", num1, "y", num2, "son:")
    for i in range(num1, num2 + 1):
        if i < 2:
            continue
        es_primo = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            print(i)

