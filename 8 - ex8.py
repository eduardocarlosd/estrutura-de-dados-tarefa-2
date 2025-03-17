def ex8(n):
    if n <= 0:
        return ''
    return ex8(n - 3) + str(n) + ex8(n - 2) + str(n)

resultado = ex8(4)
print(resultado)
