def para_romano(numero):
    numeros_romano = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    resultado = ""
    for valor, numero_romano in numeros_romano:
        while numero >= valor:
            resultado += numero_romano
            numero -= valor
    return resultado