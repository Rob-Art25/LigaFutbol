"""from modelo.jugador import Jugador
from modelo.entrenador import Entrenador"""

class ExcepcionJugador(Exception):
    pass

class ExcepcionJugadorInvalido(Exception):
    pass


class ExcepcionEntrenador(Exception):
    pass


class ExcepcionEquipoEntrenador(Exception):
    pass

class ExcepcionNombreEquipo(Exception):
    pass

class ExcepcionSancion(Exception):
    pass

class ExcepcionEstadisticasGoles(Exception):
    pass

"""class Equipo():
    
    def __init__(self, nombre):
        self.jugador = None
        self.entrenador = None
        if type(nombre) == str:
            self.nombre = nombre
        self.partidos_ganados = 0
        self.partidos_perdidos = 0
        self.partidos_empatados = 0
        self.partidos_jugados = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0
        self.sanciones = []
        self.jugadores = []   #lista de jugadores: Equipo
    
    def mostrarEquipo(self):
        
        print("Entrenador: ", self.entrenador)
        i = 1
        for jugador  in self.jugadores:
            print(f"Jugador {i}:", self.jugadores[i-1].getNombre())
            i = i + 1
        

#----------------------------------------------------------------------------------------------------------------
#-------------JUGADOR--------------------------------------------------------------------------------------------        
    def registrarJugador(self, jugador):
        try:
            if type(jugador) == Jugador:
                if jugador.getNombre() is not None and jugador.getApPaterno() is not None and jugador.getApMaterno() is not None:
                    self.jugadores.append(jugador) # agregar a la base de datos
                    print("Jugador Registrado con Éxito!")
                else:
                    raise ExcepcionJugadorInvalido("Lo que intentas registrar no es un jugador Valido!")
            else:
                raise ExcepcionJugador("Lo que intentas registrar no es un jugador!")
        except ExcepcionJugador as ej:
            print(ej)

    def actualizarJugador(self, jugador, jugadorEDT):
        for juga in self.jugadores:
            if juga == jugador:
                if type(jugadorEDT) == Jugador:
                    if jugadorEDT.getNombre() is not None and jugadorEDT.getApPaterno() is not None and jugadorEDT.getApMaterno() is not None:
                        juga.setNombre(jugadorEDT.getNombre())
                        juga.setApPaterno(jugadorEDT.getApPaterno())
                        juga.setApMaterno(jugadorEDT.getApMaterno())
                        juga.setEdad(jugadorEDT.getEdad())
                        juga.setPosicion(jugadorEDT.getPosicion())
                        return "Actualizado Con Éxito!"
                    else:
                        raise ExcepcionJugadorInvalido("No se puede cambiar, datos invalidos, vuélve a intentarlo")
                else:
                    raise ExcepcionJugadorInvalido("Lo que intentas cambiar no es de tipo jugador, verifica y vuelve a intentar")
        else:
            raise ExcepcionJugador("El jugador que intentas modificar no existe, verifica y vuelve a intentar")
        

    def darDeBajaJugador(self, jugador):
        if type(jugador) is Jugador:
            for juga in self.jugadores:
                if juga == jugador:
                    self.jugadores.remove(juga)
                    return "Baja realizada con éxito!"
            else:
                raise ExcepcionJugador("El Jugador que intentas dar de baja no existe")
        else:
            raise ExcepcionJugadorInvalido("El jugador que intentas dar de baja no es válido")

#-------------------------------------------------------------------------------------------------------------
#------------------------ENTRENADOR---------------------------------------------------------------------------
    def asignarEntrenador(self, entrenador):
        if self.entrenador == None:
            try:
                if type(entrenador) == Entrenador:
                    if entrenador.getNombre() is not None and entrenador.getApPaterno() is not None and entrenador.getApMaterno() is not None:
                        self.entrenador = entrenador # Agregar a la base de Datos
                        print("¡Entrenador Registrado con Éxito!")
                    else:
                        raise ExcepcionEntrenador("Lo que intentas Asignar no es un Entrenador Valido!")
                else:
                    raise ExcepcionEntrenador("¡Lo que intentas Asignar no es un entrenador!")
            except ExcepcionJugador as eE:
                 print(eE)
        else:
            raise  ExcepcionEquipoEntrenador("No puedes Asignar más de un entrenador a un equipo.")

    def darDeBajaEntrenador(self):
        if self.entrenador is not None:
            self.entrenador = None
            print("Baja realizada con éxito!")
        else:
            raise ExcepcionEntrenador("No puedes dar de baja a un entrenador que no existe!")

    def cambiarEntrenador(self, entrenador):
        if self.entrenador is not None:
            if type(entrenador) == Entrenador:
                self.entrenador = entrenador
            else:
                raise ExcepcionEntrenador("El Nuevo entrenador no es válido")
        else:
            raise ExcepcionEntrenador("No puedes cambiar al entrenador, no hay entrenador asignado aún")
        

    def setNombre(self, nombre):
        if type(nombre)== str:
            self.nombre = nombre
        else:
            raise ExcepcionNombreEquipo("El nombre ingresado no es válido, inténtalo de nuevo...")
    
    def getEntrenador(self):
        if self.entrenador is not None:
            return self.entrenador
    
    def getGoles_a_Favor(self):
        return self.goles_a_favor
    
    def getGoles_en_Contra(self):
        return self.goles_en_contra
    
    def getPartidosGanados(self):
        return self.partidos_ganados
    
    def getPartidosPerdidos(self):
        return self.partidos_perdidos
    
    def getSanciones(self):
        return self.sanciones
    
    def agregarSancion(self, sancion):
        if type(sancion) == str:
            self.sanciones.append[sancion]
        else:
            raise ExcepcionSancion("La Sanción no es válida")
        

    
    def actualizarEstadisticas(self, goles_a_favor, goles_en_contra):
        if type(goles_a_favor) == int and type(goles_en_contra) == int:
            self.partidos_jugados += 1
            self.goles_a_favor += goles_a_favor
            self.goles_en_contra += goles_en_contra
            if self.goles_a_favor > self.goles_en_contra:
                self.partidos_ganados += 1
            elif self.goles_a_favor == self.goles_en_contra:
                self.partidos_empatados += 1
            else:
                self.partidos_perdidos += 1
        else:
            raise ExcepcionEstadisticasGoles("Los Goles Ingresados NO son Válidos!")
        

    
    def toString(self):
        print(f"Equipo: {self.nombre}, Partidos Jugados: {self.partidos_jugados}, Partidos Ganados: {self.partidos_perdidos}, Partidos Perdidos: {self.partidos_perdidos}, Partidos Empatados: {self.partidos_empatados}")"""