def mdc(x, y):
    if y == 0:
        return x
    return mdc(y, x % y)


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"MDC de {num1} e {num2} é {mdc(num1, num2)}")
