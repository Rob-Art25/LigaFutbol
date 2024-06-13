"""from modelo.partidos import Partido, PartidoEquipoException, ExcepcionGoles, arbitroException, fechaException
from modelo.equipo import Equipo
import pytest 

def test_partido_Invalido_Equipo():
    eq1 = Equipo("Leones")
    eq2 = 25
    fecha = "25/04/2000"
    with pytest.raises(PartidoEquipoException):
        p1 = Partido(eq1, eq2, fecha)

def test_partido_Invalido_fecha():
    eq1 = Equipo("Leones")
    eq2 = Equipo("Perros")
    fecha = 12
    with pytest.raises(fechaException):
        p1 = Partido(eq1, eq2, fecha)


def test_Resultados_Goles_Invalidos():
    eq1 = Equipo("Leones")
    eq2 = Equipo("Perros")
    fecha = "25/04/2000"
    p1 = Partido(eq1, eq2, fecha)
    goles_eq1 = 3
    goles_eq2 = "Pepe"

    with pytest.raises(ExcepcionGoles):
        p1.registrarResultados(goles_eq1, goles_eq2)

def test_Resultados_Goles_Negativos():
    eq1 = Equipo("Leones")
    eq2 = Equipo("Perros")
    fecha = "25/04/2000"
    p1 = Partido(eq1, eq2, fecha)
    goles_eq1 = 3
    goles_eq2 = -5

    with pytest.raises(ExcepcionGoles):
        p1.registrarResultados(goles_eq1, goles_eq2)

def test_Resultados_Goles_Validos():
    eq1 = Equipo("Leones")
    eq2 = Equipo("Perros")
    fecha = "25/04/2000"
    p1 = Partido(eq1, eq2, fecha)
    goles_eq1 = 3
    goles_eq2 = 2
    p1.registrarResultados(goles_eq1, goles_eq2)
    assert p1.resultado == 5"""