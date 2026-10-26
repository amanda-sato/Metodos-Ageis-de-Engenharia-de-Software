def pontuacao(lancamentos):
    total = 0
    i = 0

    for jogada in range(10):
        if lancamentos[i] + lancamentos[i+1] == 10:
            total += 10 + lancamentos[i+2]
            i += 2
        else:
            total += lancamentos[i] + lancamentos[i+1]
            i += 2

    return total