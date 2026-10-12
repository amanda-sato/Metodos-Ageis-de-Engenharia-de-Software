def somar(numeros):
    if numeros == "":
        return 0
    numeros = numeros.replace("\n", ",")
    total = 0
    for parte in numeros.split(","):
        total += int(parte)
    return total
