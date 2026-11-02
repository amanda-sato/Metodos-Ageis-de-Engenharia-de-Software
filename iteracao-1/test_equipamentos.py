from datetime import date
from equipamentos import Inventario, Item

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