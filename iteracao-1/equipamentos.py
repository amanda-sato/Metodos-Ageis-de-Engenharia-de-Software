from datetime import timedelta


class ReservaRecusada(Exception):
    def __init__(self, mensagem, data_livre_seguinte=None):
        super().__init__(mensagem)
        self.data_livre_seguinte = data_livre_seguinte


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

    @property
    def itens(self):
        return [self]


class Kit:
    def __init__(self, nome, itens):
        self.nome = nome
        self.itens = itens

    @property
    def em_manutencao(self):
        return any(item.em_manutencao for item in self.itens)


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
        if (fim - inicio).days > 7:
            raise ReservaRecusada("O empréstimo não pode ter mais de 7 dias corridos.")
        for existente in self.reservas:
            partilham_itens = any(i in existente.item.itens for i in item.itens)
            if partilham_itens and inicio <= existente.fim and fim >= existente.inicio:
                data_livre = existente.fim + timedelta(days=1)
                raise ReservaRecusada(
                    f"O item já está reservado nessas datas. Fica livre a {data_livre:%d/%m/%Y}.",
                    data_livre_seguinte=data_livre,
                )
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
        self.devolucao = None