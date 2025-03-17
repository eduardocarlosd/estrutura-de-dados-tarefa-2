def contar_zeros(n):
    if n == 0:  
        return 0
    if n % 10 == 0:  
        return 1 + contar_zeros(n // 10) 
    return contar_zeros(n // 10)  

numero = int(input("Digite um número: "))
print(f"Número de zeros: {contar_zeros(numero)}")
