def contar_zeros(n):
    if n == 0:  # Caso base: se n for 0, não há mais dígitos
        return 0
    if n % 10 == 0:  # Verifica se o último dígito é zero
        return 1 + contar_zeros(n // 10)  # Conta o zero e faz recursão com o número sem o último dígito
    return contar_zeros(n // 10)  # Apenas faz recursão, ignorando o último dígito

# Exemplo de uso:
numero = int(input("Digite um número: "))
print(f"Número de zeros: {contar_zeros(numero)}")
