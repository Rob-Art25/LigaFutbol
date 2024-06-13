"""import pytest 
from modelo.jugador import Jugador

@pytest.mark.parametrize("nombre, apP, apM", [
    ('Luis', 'Perez', 'Perez'),
    ('Pedro', 'Flores', 'Linares'),
    ('Juan', "López", 'Juárez'),
    (None, None, None),
])

def test_Jugador(nombre, apP, apM):
    j1 = Jugador(nombre, apP, apM)

    assert j1.getNombre() == nombre
    assert j1.getApPaterno() == apP
    assert j1.getApMaterno() == apM

"""