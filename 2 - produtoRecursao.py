def produto(a, b):
    if b == 1:  
        return a
    return a + produto(a, b - 1)  


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"{num1} * {num2} = {produto(num1, num2)}")
