def para_romano(numero):
    if not 1 <= numero <= 3999:
        raise ValueError("O número tem de estar entre 1 e 3999")

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


def para_inteiro(numeral):
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, letra in enumerate(numeral):
        valor = valores[letra]
        if i + 1 < len(numeral) and valor < valores[numeral[i + 1]]:
            total -= valor
        else:
            total += valor
    return total