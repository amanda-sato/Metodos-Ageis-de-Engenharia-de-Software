def somar(numeros):
    if numeros == "":
        return 0
    if numeros.startswith("//"):
        numeros = numeros[4:].replace(numeros[2], ",")
    total = 0
    negativos = []
    for parte in numeros.split(","):
        if int(parte) < 0:
            negativos.append(parte)
        total += int(parte)
    if negativos:
        raise ValueError("negativos não são permitidos: " + ",".join(negativos))
    return total