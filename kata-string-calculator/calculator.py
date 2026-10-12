def somar(numeros):
    if numeros == "":
        return 0
    if numeros.startswith("//"):
        numeros = numeros[4:].replace(numeros[2], ",")
    total = 0
    for parte in numeros.split(","):
        total += int(parte)
    return total