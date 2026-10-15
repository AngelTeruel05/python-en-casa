num1 = int(input("Introduce primer número: "))
num2 = int(input("Introduce segundo número: "))

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)
    
while num1 <= num2:
    if num1 % 2 == 0:
        print(num1)
    num1 += 1