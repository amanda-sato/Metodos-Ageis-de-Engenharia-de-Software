from datetime import date
from equipamentos import Inventario, Item


def test_dado_item_com_devolucao_a_20_quando_consulto_a_17_entao_faltam_3_dias():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    inventario.registrar(camera)
    reserva = inventario.reservar(camera, date(2026, 11, 15), date(2026, 11, 20))
    inventario.levantar(reserva)

    emprestimos = inventario.consultar_emprestimos(hoje=date(2026, 11, 17))

    assert [(e.item.nome, e.situacao) for e in emprestimos] == [
        ("Câmera Digital", "faltam 3 dias"),
    ]


def test_item_com_devolucao_hoje_quando_consulto_os_emprestimos():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    inventario.registrar(camera)
    reserva = inventario.reservar(camera, date(2026, 11, 15), date(2026, 11, 20))
    inventario.levantar(reserva)

    emprestimos = inventario.consultar_emprestimos(hoje=date(2026, 11, 20))

    assert [(e.item.nome, e.situacao) for e in emprestimos] == [
        ("Câmera Digital", "termina hoje"),
    ]

def test_dado_item_com_prazo_expirado_quando_consulto_os_emprestimo():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    inventario.registrar(camera)
    reserva = inventario.reservar(camera, date(2026, 11, 15), date(2026, 11, 20))
    inventario.levantar(reserva)

    emprestimos = inventario.consultar_emprestimos(hoje=date(2026, 11, 22))

    assert [(e.item.nome, e.situacao) for e in emprestimos] == [
        ("Câmera Digital", "em atraso"),
    ]