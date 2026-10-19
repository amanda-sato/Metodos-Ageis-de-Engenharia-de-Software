def para_romano(numero):
    numeros_romano = [(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    resultado = ""
    for valor, numero_romano in numeros_romano:
        while numero >= valor:
            resultado += numero_romano  
            numero -= valor
    return resultado