class Item:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
class ResultadoBuscaLista:
    def __init__(self, itens, mensagem):
        self.itens = itens
        self.mensagem = mensagem


class Inventario:
    def registrar(self, item):
        pass

    def consultar_lista(self):
        return ResultadoBuscaLista([], "Não há equipamentos registrados.")


