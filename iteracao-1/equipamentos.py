class ReservaRecusada(Exception):
    pass


class Item:
    def __init__(self, nome, tipo, em_manutencao=False):
        self.nome = nome
        self.tipo = tipo
        self.em_manutencao = em_manutencao

    @property
    def estado(self):
        if self.em_manutencao:
            return "indisponível"
        return "disponível"


class ResultadoBuscaLista:
    def __init__(self, itens, mensagem):
        self.itens = itens
        self.mensagem = mensagem


class Inventario:
    def __init__(self):
        self.itens = []
        self.reservas = []

    def registrar(self, item):
        self.itens.append(item)

    def reservar(self, item, inicio, fim):
        if item.em_manutencao:
            raise ReservaRecusada("O item está em manutenção.")
        reserva = Reserva(item, inicio, fim)
        self.reservas.append(reserva)
        return reserva

    def consultar_lista(self):
        if not self.itens:
            return ResultadoBuscaLista([], "Não há equipamentos registrados.")
        return ResultadoBuscaLista(list(self.itens), None)


class Reserva:
    def __init__(self, item, inicio, fim):
        self.item = item
        self.inicio = inicio
        self.fim = fim