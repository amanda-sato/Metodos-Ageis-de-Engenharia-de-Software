class Jogo:
    def __init__(self):
        self.lancamentos = []

    def lancar(self, pinos):
        self.lancamentos.append(pinos)

    def pontuacao(self):
        lancamentos = self.lancamentos
        total = 0
        i = 0

        for jogada in range(10):
            if lancamentos[i] == 10:
                total += 10 + lancamentos[i+1] + lancamentos[i+2]
                i += 1
            elif lancamentos[i] + lancamentos[i+1] == 10:
                total += 10 + lancamentos[i+2]
                i += 2
            else:
                total += lancamentos[i] + lancamentos[i+1]
                i += 2

        return total