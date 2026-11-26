from datetime import date
import pytest
from equipamentos import Inventario, Item, ReservaRecusada


def test_utilizador_com_item_em_atraso_quando_tenta_reservar_recusa_indicando_o_item():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    tripe = Item("Tripé grande", "tripé")
    inventario.registrar(camera)
    inventario.registrar(tripe)
    reserva = inventario.reservar(
        camera, date(2026, 11, 15), date(2026, 11, 20), utilizador="Ana"
    )
    inventario.levantar(reserva)

    with pytest.raises(ReservaRecusada, match="Câmera Digital"):
        inventario.reservar(
            tripe, date(2026, 11, 25), date(2026, 11, 27),
            utilizador="Ana", hoje=date(2026, 11, 22),
        )

    assert len(inventario.reservas) == 1

def test_utilizador_bloqueado_quando_o_item_em_atraso_e_devolvido_e_volta_a_poder_reservar():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    tripe = Item("Tripé grande", "tripé")
    inventario.registrar(camera)
    inventario.registrar(tripe)
    reserva = inventario.reservar(
        camera, date(2026, 11, 15), date(2026, 11, 20), utilizador="Ana"
    )
    inventario.levantar(reserva)
    with pytest.raises(ReservaRecusada):
        inventario.reservar(
            tripe, date(2026, 11, 25), date(2026, 11, 27),
            utilizador="Ana", hoje=date(2026, 11, 22),
        )

    inventario.devolver(reserva)

    inventario.reservar(
        tripe, date(2026, 11, 25), date(2026, 11, 27),
        utilizador="Ana", hoje=date(2026, 11, 22),
    )
    assert len(inventario.reservas) == 2


def test_utilizador_com_dois_itens_em_atraso_quando_devolve_so_um_continua_bloqueado():
    inventario = Inventario()
    camera = Item("Câmera Digital", "câmera")
    microfone = Item("Microfone 1", "microfone")
    tripe = Item("Tripé grande", "tripé")
    for item in [camera, microfone, tripe]:
        inventario.registrar(item)
    reserva_camera = inventario.reservar(
        camera, date(2026, 11, 15), date(2026, 11, 20), utilizador="Ana"
    )
    reserva_microfone = inventario.reservar(
        microfone, date(2026, 11, 15), date(2026, 11, 20), utilizador="Ana"
    )
    inventario.levantar(reserva_camera)
    inventario.levantar(reserva_microfone)

    inventario.devolver(reserva_camera)

    with pytest.raises(ReservaRecusada, match="Microfone 1"):
        inventario.reservar(
            tripe, date(2026, 11, 25), date(2026, 11, 27),
            utilizador="Ana", hoje=date(2026, 11, 22),
        )