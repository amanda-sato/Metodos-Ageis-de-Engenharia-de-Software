def pontuacao(lancamentos):
    total = 0
    i = 0

    for jogada in range(10):
        if lancamentos[i] == 10:  # strike
            total += 10 + lancamentos[i+1] + lancamentos[i+2]
            i += 1
        elif lancamentos[i] + lancamentos[i+1] == 10:  # spare
            total += 10 + lancamentos[i+2]
            i += 2
        else: # jogada livre                                          
            total += lancamentos[i] + lancamentos[i+1]
            i += 2

    return total