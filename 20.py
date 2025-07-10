def intercalar_listas(lista1, lista2):
    return [item for par in zip(lista1, lista2) for item in par]
