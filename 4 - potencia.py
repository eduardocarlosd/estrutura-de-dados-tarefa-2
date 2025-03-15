def potencia(b, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / potencia(b, -n)
    return b * potencia(b, n - 1)


base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

print(f"{base}^{expoente} =", potencia(base, expoente))
