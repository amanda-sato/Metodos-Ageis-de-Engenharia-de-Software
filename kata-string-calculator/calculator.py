def somar(numeros):
    if numeros == "":
        return 0
    if numeros.startswith("//"):
        cabecalho, numeros = numeros[2:].split("\n", 1)
        for separador in cabecalho.strip("[]").split("]["):
            numeros = numeros.replace(separador, ",")
    total = 0
    negativos = []
    for parte in numeros.split(","):
        if int(parte) < 0:
            negativos.append(parte)
        if int(parte) <= 1000:
            total += int(parte)
    if negativos:
        raise ValueError("negativos não são permitidos: " + ",".join(negativos))
    return total