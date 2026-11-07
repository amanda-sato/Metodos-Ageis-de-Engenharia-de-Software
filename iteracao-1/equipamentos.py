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
    def __init__(self, feriados=None):
        self.itens = []
        self.reservas = []
        self.feriados = feriados or []

    def registrar(self, item):
        self.itens.append(item)

    def reservar(self, item, inicio, fim, perfil="estudante", hoje=None):
        if item.em_manutencao:
            raise ReservaRecusada("O item está em manutenção.")
        if (fim - inicio).days > 7:
            raise ReservaRecusada("O empréstimo não pode ter mais de 7 dias corridos.")
        canceladas = []
        for existente in self.reservas:
            partilham_itens = any(i in existente.item.itens for i in item.itens)
            if partilham_itens and inicio <= existente.fim and fim >= existente.inicio:
                if self.docente_pode_passar_a_frente(existente, perfil, hoje):
                    canceladas.append(existente)
                    continue
                data_livre = existente.fim + timedelta(days=1)
                raise ReservaRecusada(
                    f"O item já está reservado nessas datas. Fica livre a {data_livre:%d/%m/%Y}.",
                    data_livre_seguinte=data_livre,
                )
        for cancelada in canceladas:
            self.reservas.remove(cancelada)
        reserva = Reserva(item, inicio, fim, self.dia_de_devolucao(fim), perfil)
        self.reservas.append(reserva)
        return reserva

    def docente_pode_passar_a_frente(self, existente, perfil, hoje):
        return (
            perfil == "docente"
            and existente.perfil == "estudante"
            and hoje is not None
            and (existente.inicio - hoje).days > 2
        )

    def dia_de_devolucao(self, fim):
        devolucao = fim
        while devolucao in self.feriados:
            devolucao += timedelta(days=1)
        return devolucao

    def estado_em(self, item, data):
        for reserva in self.reservas:
            if item in reserva.item.itens and reserva.inicio <= data <= reserva.fim:
                if reserva.perfil == "docente":
                    return "indisponível"
                return "em espera"
        return "disponível"

    def consultar_lista(self):
        if not self.itens:
            return ResultadoBuscaLista([], "Não há equipamentos registrados.")
        return ResultadoBuscaLista(list(self.itens), None)


class Reserva:
    def __init__(self, item, inicio, fim, devolucao, perfil):
        self.item = item
        self.inicio = inicio
        self.fim = fim
        self.devolucao = devolucao
        self.perfil = perfil