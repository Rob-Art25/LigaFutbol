"""from modelo.ligas import Liga, EquipoException, FechaException, PartidoException, sancionException
from modelo.equipo import Equipo
from modelo.partidos import Partido
import pytest 

def test_Liga_Invalida():
    eq1 = Equipo("Perros")
    eq2 = 25
    with pytest.raises(EquipoException):
        l1 = Liga(eq1, eq2)

def test_generarPartido_Equipo_Invalido():
    eq1 = Equipo("Linces")
    eq2 = 25
    eq3 = Equipo("Lobos")
    fecha = "12/02/2021"
    liga1 = Liga(eq1, eq3)
    with pytest.raises(EquipoException):
        liga1.generarPartido(eq1, eq2, fecha)

def test_generarPartido_Invalido_Fecha():
    eq1 = Equipo("Linces")
    eq2 = Equipo("Lobos")
    fecha = 23
    liga1 = Liga(eq1, eq2)
    with pytest.raises(FechaException):
        liga1.generarPartido(eq1, eq2, fecha)

def test_generarPartido_Valido():
    eq1 = Equipo("Linces")
    eq2 = Equipo("Lobos")
    fecha = "14/02/2021"
    liga1 = Liga(eq1, eq2)
    partido = liga1.generarPartido(eq1, eq2, fecha)
    assert liga1.partidos[0] == partido


def test_cancelarPartido_InValido():
    eq1 = Equipo("Perrazos")
    eq2 = Equipo("Los Papuhs")
    liga = Liga(eq1, eq2)
    partido = 25
    with pytest.raises(PartidoException):
        liga.cancelarPartido(partido)

def test_cancelarPartido_InExistente():
    eq1 = Equipo("Perrazos")
    eq2 = Equipo("Los Papuhs")
    liga = Liga(eq1, eq2)
    partido = Partido(eq1, eq2, "La Fecha")
    with pytest.raises(PartidoException):
        liga.cancelarPartido(partido)

def test_cancelarPartido_Valido():
    eq1 = Equipo("Perrazos")
    eq2 = Equipo("Los Papuhs")
    liga = Liga(eq1, eq2)
    partido = liga.generarPartido(eq1, eq2, "La Fecha")
    print("Equipo 1: ", partido.equipo1.nombre)
    print("Equipo 2: ", partido.equipo2.nombre)
    print("Fecha: ", partido.fecha)
    liga.cancelarPartido(partido)
    assert len(liga.cancelados) == 1
    assert len(liga.partidos) == 0

def test_disputarPartido_Valido():
    eq1 = Equipo("Perrazos")
    eq2 = Equipo("Los Papuhs")
    liga = Liga(eq1, eq2)
    partido = liga.generarPartido(eq1, eq2, "La Fecha")
    golesEq1 = 2
    golesEq2 = 3
    print("Equipo 1: ", partido.equipo1.nombre)
    print("Equipo 2: ", partido.equipo2.nombre)
    print("Fecha: ", partido.fecha)
    liga.disputarPartido(partido, golesEq1, golesEq2)
    assert liga.partidos[0].resultado == 5

def test_disputarPartido_InValido():
    eq1 = Equipo("Perrazos")
    eq2 = Equipo("Los Papuhs")
    liga = Liga(eq1, eq2)
    partido = 25
    golesEq1 = 2
    golesEq2 = 3
    with pytest.raises(PartidoException):
        liga.disputarPartido(partido, golesEq1, golesEq2)

def test_disputarPartido_InExistente():
    eq1 = Equipo("Perrazos")
    eq2 = Equipo("Los Papuhs")
    eq3 = Equipo("Pumas")
    liga = Liga(eq1, eq2)
    partido = Partido(eq1, eq2, "La Fecha")
    liga.generarPartido(eq1, eq3, "12/03/2022")
    golesEq1 = 2
    golesEq2 = 3
    with pytest.raises(PartidoException):
        liga.disputarPartido(partido, golesEq1, golesEq2)


#-------------------Sanciones---------------
#-------------------------------------------
"""
