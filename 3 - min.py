def minimo(arr, n):
    if n == 1:
        return arr[0]
    return min(arr[n - 1], minimo(arr, n - 1))

lista = [3, 7, 2, 9, 5]
print("Menor elemento:", minimo(lista, len(lista)))
