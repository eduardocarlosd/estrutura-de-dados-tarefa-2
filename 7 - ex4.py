def ex7(n):
    if n < 0:
        return
    print(n)
    ex7(n - 2)
    ex7(n - 3)
    print(n)


ex7(4)
