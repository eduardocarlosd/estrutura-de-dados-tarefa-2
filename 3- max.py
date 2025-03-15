def maximo(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], maximo(arr, n - 1))


lista = [3, 7, 2, 9, 5]
print("Maior elemento:", maximo(lista, len(lista)))
