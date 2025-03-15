def soma(a, b):
    if b == 0:  
        return a
    return soma(a + 1, b - 1)  

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"{num1} + {num2} = {soma(num1, num2)}")
