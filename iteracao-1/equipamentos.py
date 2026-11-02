class Item:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo


class ResultadoBuscaLista:
    def __init__(self, itens, mensagem):
        self.itens = itens
        self.mensagem = mensagem


class Inventario:
    def __init__(self):
        self.itens = []

    def registrar(self, item):
        self.itens.append(item)

    def consultar_lista(self):
        if not self.itens:
            return ResultadoBuscaLista([], "Não há equipamentos registrados.")
        return ResultadoBuscaLista(self.itens, None)