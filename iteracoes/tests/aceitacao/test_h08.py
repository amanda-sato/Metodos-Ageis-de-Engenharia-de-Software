from datetime import date
from equipamentos import Inventario, Item


def test_emprestimo_com_devolucao_20_quando_chega_dia_19_entao_alerta_termina_amanha():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    inventario.registrar(camera)
    reserva = inventario.reservar(camera, date(2026, 11, 15), date(2026, 11, 20))
    inventario.levantar(reserva)

    alertas = inventario.alertas_em(hoje=date(2026, 11, 19))

    assert [(a.item.nome, a.mensagem) for a in alertas] == [
        ("Câmera Digital", "O prazo termina amanhã."),
    ]


def test_emprestimo_com_devolucao_a_20_quando_chega_dia_20_alerta_termina_hoje():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    inventario.registrar(camera)
    reserva = inventario.reservar(camera, date(2026, 11, 15), date(2026, 11, 20))
    inventario.levantar(reserva)

    alertas = inventario.alertas_em(hoje=date(2026, 11, 20))

    assert [(a.item.nome, a.mensagem) for a in alertas] == [
        ("Câmera Digital", "O prazo termina hoje."),
    ]


def test_dado_item_devolvido_antes_do_prazo_fim_do_prazo_sem_alerta():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    inventario.registrar(camera)
    reserva = inventario.reservar(camera, date(2026, 11, 15), date(2026, 11, 20))
    inventario.levantar(reserva)
    inventario.devolver(reserva)

    alertas = inventario.alertas_em(hoje=date(2026, 11, 20))

    assert alertas == []