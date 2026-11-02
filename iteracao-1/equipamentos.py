class ResultadoBuscaLista:
    def __init__(self, mensagem):
        self.mensagem = mensagem


class Inventario:
    def consultar_lista(self):
        return ResultadoBuscaLista("Não há equipamentos registrados.")