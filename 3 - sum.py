def soma(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + soma(arr, n - 1)


lista = [3, 7, 2, 9, 5]
print("Soma dos elementos:", soma(lista, len(lista)))
