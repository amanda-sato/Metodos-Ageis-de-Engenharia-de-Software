from equipamentos import Inventario

#H01

def test_lista_vazia_mostra_mensagem_sem_equipamento():
    inventario = Inventario()
    resultado = inventario.consultar_lista()
    assert resultado.mensagem == "Não há equipamentos registrados."