"""from modelo.equipo import Equipo"""

class PartidoEquipoException(Exception):
    pass
class ExcepcionGoles(Exception):
    pass

class arbitroException(Exception):
    pass

class fechaException(Exception):
    pass

"""class Partido():

    def __init__(self, equipo1, equipo2, fecha):
        self.goles_equipo1 = []
        self.goles_equipo2 = []
        if type(fecha) is str:
            self.fecha = fecha
        else:
            raise fechaException("La fecha no es válida!")
 
        if type(equipo1) == Equipo and type(equipo2) == Equipo:
            if equipo1.nombre is not None and equipo2.nombre is not None:
                self.equipo1 = equipo1
                self.equipo2 = equipo2
            else:
                raise PartidoEquipoException("El Equipo que intentas registrar NO es Válido!")
        else:
            raise PartidoEquipoException("Lo que intentas registrar NO es un equipo!")
        
        self.resultado = 0
        self.arbitro = None
    
    def registrarResultados(self, goles_equipo1, goles_equipo2):
        if type(goles_equipo1) == int and type(goles_equipo2) == int and (goles_equipo1) >= 0 and (goles_equipo2) >= 0:
            self.equipo1.actualizarEstadisticas(goles_equipo1, goles_equipo2)
            self.equipo2.actualizarEstadisticas(goles_equipo2, goles_equipo1)
            self.resultado = goles_equipo1 + goles_equipo2
        else:
            raise ExcepcionGoles("Los Goles ingresados NO son Válidos!")
        
    def asignarArbitro(self, arbitro):
        if type(arbitro) == Arbitro:
            self.arbitro = arbitro
        else:
            raise arbitroException("Lo Que Intentas Asignar al Partido NO es un Arbitro!")
    
    def toString(self):
        print(f"Partido entre Equipo 1: {self.equipo1.toString()} y el Equipo 2: {self.equipo2.toString()}el día Fecha: {self.fecha}")"""