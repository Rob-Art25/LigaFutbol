import pytest
from modelo.postSQLConfig import PostgresDB
from flask import Flask
from controlador.DOM_Liga import ExcepcionJugador, ExcepcionEntrenador, ExcepcionNombreEquipo, fechaException, crearApp

pgdb = PostgresDB()

#carga los metodos de las vistas

@pytest.fixture(scope="session")
def app():
    # Setup de la aplicación 
    app = crearApp()
    app.config.update({
        "TESTING": True,
    })

    # Inicialización de la base de datos
    print("...inicializando entorno de TESTING...")
    pgdb.init_app(app)
    pgdb.create_all_tables()

    yield app
    # apartir de aquí se pone el código para liberar los recursos 

    # teardown limpiar/ reinicializar


@pytest.fixture(scope="session")
def client(app):
    print("creando cliente...")
    return app.test_client()


#--------------------------------------------------
# Test de las transacciones de la aplicación
#--------------------------------------------------

def test_login(app, client):
    with client:
        usuario = 'roberto'
        password = '12345'
        response = client.post("/login", data={"usuario":  usuario , "contrasena": password}, follow_redirects=True)
        assert response.status_code == 200 


def test_login_failed(app, client):

    with client:
        # Si las credenciales fallaron la página retorna un codigo 401
        usuario = 'pepe'
        password = '12345'
        response = client.post("/login", data={"usuario":  usuario , "contrasena": password}, follow_redirects=True)
        assert response.status_code == 401


def test_inicio_home(app, client):
    with client:
        response = client.get("/inicio", follow_redirects=True)
        assert response.status_code == 200 

#----------------------Equipos---------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

def test_registrarJugador(app, client):
    with client:
        nombre = 'pepe'
        apP = 'pepe'
        apM = 'pepe'
        response = client.post("/registrarJugador", data={"nombre":  nombre  , "apPaterno": apP, "apMaterno": apM}, follow_redirects=True)
        # Checa si la operación fue exitosa
        assert response.status_code == 200 
        #Checa que los datos insertados sean los correctos por medio de una consulta y revisión con los datos esperados
        with pgdb.get_cursor() as cursor:
            # Ejecutar una consulta
            cursor.execute("SELECT id, NOMBRE, APPATERNO, APMATERNO FROM jugadores ORDER BY 1 DESC LIMIT 1;")
            # Obtener los resultados
            registro = cursor.fetchone()
            #precio = 501 forzar que falle la prueba
            print(registro)
            assert registro[1] == nombre
            assert registro[2] == apP
            assert registro[3] == apM

def test_consulta_jugador(app, client):
    res = client.get("/consultar_jugadores", follow_redirects=True)
    assert res.status_code == 200

def test_registrar_Jugador_Nombre_Vacio(client):
            with client:
                nombre = ''
                apP = 'perez'
                apM = 'perez'
            with pytest.raises(ExcepcionJugador):
                client.post("/registrarJugador", data={"nombre": nombre, "apPaterno": apP, "apMaterno": apM}, follow_redirects=True)

def test_registrar_Jugador_ApellidoPaterno_NULO(client):
            with client:
                nombre = 'Paco'
                apP = ''
                apM = 'perez'
            with pytest.raises(ExcepcionJugador):
                client.post("/registrarJugador", data={"nombre": nombre, "apPaterno": apP, "apMaterno": apM}, follow_redirects=True)

def test_registrar_Jugador_ApellidoMaterno_NULO(client):
            with client:
                nombre = 'paco'
                apP = 'perez'
                apM = ''
            with pytest.raises(ExcepcionJugador):
                client.post("/registrarJugador", data={"nombre": nombre, "apPaterno": apP, "apMaterno": apM}, follow_redirects=True)


@pytest.mark.skip("Las consultas no Generan Error, pueden tener contenido o estar vacías. y nunca tendrán datos erroneos por que provienen de una base de datos que valida antes de registrarlos.")
def test_consulta_jugador_invalido():
    pass
    

def test_registrarEntrenador(app, client):
    with client:
        nombre = 'pepe'
        apP = 'pepe'
        apM = 'pepe'
        response = client.post("/registrarEntrenador", data={"nombre":  nombre  , "apPaterno": apP, "apMaterno": apM}, follow_redirects=True)
        # Checa si la operación fue exitosa
        assert response.status_code == 200 
        #Checa que los datos insertados sean los correctos por medio de una consulta y revisión con los datos esperados
        with pgdb.get_cursor() as cursor:
            # Ejecutar una consulta
            cursor.execute("SELECT id, NOMBRE, APPATERNO, APMATERNO FROM entrenadores ORDER BY 1 DESC LIMIT 1;")
            # Obtener los resultados
            registro = cursor.fetchone()
            #precio = 501 forzar que falle la prueba
            print(registro)
            assert registro[1] == nombre
            assert registro[2] == apP
            assert registro[3] == apM

def test_registrar_Entrenador_Nombre_Vacio():
    pass

def test_registrar_Entrenador_ApellidoPaterno_NULO():
    pass
def test_registrar_Entrenador_ApellidoMaterno_NULO():
    pass

#Las consultas: Entrenador, Jugador, Equipo, Partido y Liga sí pueden estar vacías por lo que no hay ningún momento en el que puedan causar una excepción
def test_consulta_entrenador(app, client):
    res = client.get("/consultar_entrenadores", follow_redirects=True)
    assert res.status_code == 200

@pytest.mark.skip("Las consultas no Generan Error, pueden tener contenido o estar vacías. y nunca tendrán datos erroneos por que provienen de una base de datos que valida antes de registrarlos.")
def test_consulta_entrenador_invalido():
    pass

def test_registrarEquipo(app, client):
    with client:
        nombre = 'Lobos'
        response = client.post("/registrarEquipo", data={"nombre":  nombre}, follow_redirects=True)
        # Checa si la operación fue exitosa
        assert response.status_code == 200 
        #Checa que los datos insertados sean los correctos por medio de una consulta y revisión con los datos esperados
        with pgdb.get_cursor() as cursor:
            # Ejecutar una consulta
            cursor.execute("SELECT id, NOMBRE FROM equipos ORDER BY 1 DESC LIMIT 1;")
            # Obtener los resultados
            registro = cursor.fetchone()
            #precio = 501 forzar que falle la prueba
            print(registro)
            assert registro[1] == nombre

def test_registrar_Equipo_Nombre_NULO(client):
        with client:
            nombre = ''
        with pytest.raises(ExcepcionNombreEquipo):
            client.post("/registrarEquipo", data={"nombre": nombre}, follow_redirects=True)

#Las consultas: Entrenador, Jugador, Equipo, Partido y Liga sí pueden estar vacías por lo que no hay ningún momento en el que puedan causar una excepción
def test_consultar_equipos(app, client):
    res = client.get("/consultar_equipos", follow_redirects=True)
    assert res.status_code == 200

@pytest.mark.skip("Las consultas no Generan Error, pueden tener contenido o estar vacías. y nunca tendrán datos erroneos por que provienen de una base de datos que valida antes de registrarlos.")
def test_consulta_equipo_invalido(client):
    pass
    
#------------------------------Ligas-------------------------------------------------------
#-------------------------------------------------------------------------------------
# ------- Probar Cadena Vacia---------------------------------------------------------

def test_registrarLiga(app, client):
    with client:
        eq1 = 'Lobos'
        eq2 = 'Linces'
        response = client.post("/registrarLiga", data={"equipo1":  eq1, "equipo2": eq2}, follow_redirects=True)
        # Checa si la operación fue exitosa
        assert response.status_code == 200 
        #Checa que los datos insertados sean los correctos por medio de una consulta y revisión con los datos esperados
        with pgdb.get_cursor() as cursor:
            # Ejecutar una consulta
            cursor.execute("SELECT id, EQUIPO1, EQUIPO2 FROM Ligas ORDER BY 1 DESC LIMIT 1;")
            # Obtener los resultados
            registro = cursor.fetchone()
            #precio = 501 forzar que falle la prueba
            print(registro)
            assert registro[1] == eq1
            assert registro[2] == eq2

def test_registrar_Liga_NombreEquipo1_Vacio(client):
        with client:
            eq1 = ''
            eq2 = 'lobos'
        with pytest.raises(ExcepcionNombreEquipo):
            client.post("/registrarLiga", data={"equipo1": eq1, "equipo2": eq2}, follow_redirects=True)


def test_registrar_Liga_NombreEquipo2_Vacio(client):
    with client:
            eq1 = 'perros'
            eq2 = ''
    with pytest.raises(ExcepcionNombreEquipo):
            client.post("/registrarLiga", data={"equipo1": eq1, "equipo2": eq2}, follow_redirects=True)

#Las consultas: Entrenador, Jugador, Equipo, Partido y Liga sí pueden estar vacías por lo que no hay ningún momento en el que puedan causar una excepción
def test_consultar_ligas(app, client):
    res = client.get("/consultar_Ligas", follow_redirects=True)
    assert res.status_code == 200

@pytest.mark.skip("Las consultas no Generan Error, pueden tener contenido o estar vacías. y nunca tendrán datos erroneos por que provienen de una base de datos que valida antes de registrarlos.")
def test_consulta_liga_invalida():
    pass

def test_registrarPartido(app, client):
    with client:
        eq1 = 'Lobos'
        eq2 = 'Linces'
        fecha = '12/02/2022'
        response = client.post("/registrarPartido", data={"equipo1":  eq1, "equipo2": eq2, "fecha": fecha}, follow_redirects=True)
        # Checa si la operación fue exitosa
        assert response.status_code == 200 
        #Checa que los datos insertados sean los correctos por medio de una consulta y revisión con los datos esperados
        with pgdb.get_cursor() as cursor:
            # Ejecutar una consulta
            cursor.execute("SELECT id, EQUIPO1, EQUIPO2 FROM Partidos ORDER BY 1 DESC LIMIT 1;")
            # Obtener los resultados
            registro = cursor.fetchone()
            #precio = 501 forzar que falle la prueba
            print(registro)
            assert registro[1] == eq1
            assert registro[2] == eq2

def test_registrar_Partido_NombreEquipo1_Vacio(client):
        with client:
            eq1 = ''
            eq2 = 'lobos'
            fecha = '12/10/2012'
        with pytest.raises(ExcepcionNombreEquipo):
            client.post("/registrarPartido", data={"equipo1": eq1, "equipo2": eq2, "fecha": fecha}, follow_redirects=True)


def test_registrar_Partido_NombreEquipo2_NULO(client):
        with client:
            eq1 = 'perros'
            eq2 = ''
            fecha = '12/12/2020'
        with pytest.raises(ExcepcionNombreEquipo):
            client.post("/registrarPartido", data={"equipo1": eq1, "equipo2": eq2, "fecha": fecha}, follow_redirects=True)


def test_registrar_Partido_Fecha_NULO(client):
    with client:
        eq1 = 'perros'
        eq2 = 'lobos'
        fecha = ''
        with pytest.raises(fechaException):
            client.post("/registrarPartido", data={"equipo1": eq1, "equipo2": eq2, "fecha": fecha}, follow_redirects=True)

#Las consultas: Entrenador, Jugador, Equipo, Partido y Liga sí pueden estar vacías por lo que no hay ningún momento en el que puedan causar una excepción
def test_consultar_partidos(client):
    res = client.get("/consultar_Partidos", follow_redirects=True)
    assert res.status_code == 200

@pytest.mark.skip("Las consultas no Generan Error, pueden tener contenido o estar vacías. y nunca tendrán datos erroneos por que provienen de una base de datos que valida antes de registrarlos.")
def test_consulta_partido_invalido():
    pass