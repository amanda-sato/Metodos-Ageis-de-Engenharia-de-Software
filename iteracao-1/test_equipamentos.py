from datetime import date
import pytest
from equipamentos import Inventario, Item, ReservaRecusada, Kit

#H01

def test_lista_vazia_mostra_mensagem_sem_equipamento():
    inventario = Inventario()
    resultado = inventario.consultar_lista()
    assert resultado.mensagem == "Não há equipamentos registrados."


def test_lista_nome_e_tipo_de_cada_item():
    inventario = Inventario()
    inventario.registrar(Item("Câmera Digital", "câmera"))
    inventario.registrar(Item("Tripé grande", "tripé"))
    inventario.registrar(Item("Câmera Kodak", "câmera"))

    resultado = inventario.consultar_lista()

    nomes_e_tipos = [(item.nome, item.tipo) for item in resultado.itens]
    assert nomes_e_tipos == [("Câmera Digital", "câmera"), ("Tripé grande", "tripé"), ("Câmera Kodak", "câmera")]


def test_item_em_manutencao_indisponivel():
    inventario = Inventario()
    inventario.registrar(Item("Câmera Digital", "câmera"))
    inventario.registrar(Item("Câmera Kodak", "câmera", em_manutencao=True))

    resultado = inventario.consultar_lista()

    estados = [(item.nome, item.estado) for item in resultado.itens]
    assert estados == [
        ("Câmera Digital", "disponível"),
        ("Câmera Kodak", "indisponível"),
    ]


# H02

def test_reservar_item_disponivel_regista_reserva_com_as_datas():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    inventario.registrar(camera)

    inventario.reservar(camera, date(2026, 10, 5), date(2026, 10, 8))

    reservas = [(r.item.nome, r.inicio, r.fim) for r in inventario.reservas]
    assert reservas == [("Câmera Digital", date(2026, 10, 5), date(2026, 10, 8))]


def test_reservar_item_em_manutencao_e_recusado():
    inventario = Inventario()
    camera = Item("Câmera Kodak", "câmera", em_manutencao=True)
    inventario.registrar(camera)

    with pytest.raises(ReservaRecusada):
        inventario.reservar(camera, date(2026, 10, 5), date(2026, 10, 8))

    assert inventario.reservas == []

def test_reservar_mais_de_sete_dias_e_recusado_com_indicacao_do_limite():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    inventario.registrar(camera)

    with pytest.raises(ReservaRecusada, match="7 dias"):
        inventario.reservar(camera, date(2026, 11, 10), date(2026, 11, 18))

    assert inventario.reservas == []


# H03

def test_reserva_sobreposta_e_recusada_com_data_livre_seguinte():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    inventario.registrar(camera)
    inventario.reservar(camera, date(2026, 10, 5), date(2026, 10, 8))

    with pytest.raises(ReservaRecusada) as erro:
        inventario.reservar(camera, date(2026, 10, 7), date(2026, 10, 10))

    assert erro.value.data_livre_seguinte == date(2026, 10, 9)
    assert len(inventario.reservas) == 1

def test_reserva_a_partir_do_dia_seguinte_ao_fim_e_aceite(): # passou de primeira
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    inventario.registrar(camera)
    inventario.reservar(camera, date(2026, 10, 5), date(2026, 10, 8))

    inventario.reservar(camera, date(2026, 10, 9), date(2026, 10, 12))

    assert len(inventario.reservas) == 2


def test_reservar_item_de_kit_reservado_e_recusado():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    tripe = Item("Tripé grande", "tripé")
    inventario.registrar(camera)
    inventario.registrar(tripe)
    kit = Kit("Kit vídeo", [camera, tripe])
    inventario.reservar(kit, date(2026, 10, 5), date(2026, 10, 8))

    with pytest.raises(ReservaRecusada):
        inventario.reservar(camera, date(2026, 10, 5), date(2026, 10, 8))

    assert len(inventario.reservas) == 1


# H05

def test_reserva_de_sete_dias_e_aceite_com_devolucao_no_ultimo_dia():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    inventario.registrar(camera)

    reserva = inventario.reservar(camera, date(2026, 11, 10), date(2026, 11, 17))

    assert reserva.devolucao == date(2026, 11, 17)