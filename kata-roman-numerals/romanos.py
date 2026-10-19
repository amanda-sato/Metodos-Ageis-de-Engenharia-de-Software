def para_romano(numero):
    if numero < 5:
        return "I" * numero
    elif numero < 9:
        return "V" + "I" * (numero - 5)
    elif numero == 10:
        return "X"