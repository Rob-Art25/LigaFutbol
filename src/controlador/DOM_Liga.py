from flask import render_template, request, redirect, url_for
from modelo.postSQLConfig import PostgresDB
from modelo.equipo import ExcepcionJugador, ExcepcionEntrenador, ExcepcionNombreEquipo
from modelo.partidos import fechaException
from flask import Flask
# Importar Base de Datos...

USUARIOS = {
    'roberto': '12345',
    'mariano': '12345'
}

def registrarRutas(app):
    

        #----------------------------------------
        # Página de registro al sistema
        #----------------------------------------
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/login', methods=['GET', 'POST'])
    def login_home():
        error = None
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['contrasena']
            if username in USUARIOS and USUARIOS[username] == password:
                # Iniciar sesión exitosa, redirigir a otra página
                return redirect(url_for('inicio'))
            else:
                # Credenciales incorrectas, mostrar mensaje de error
                #return 'Credenciales incorrectas. <a href="/login">Intenta de nuevo</a>'
                msj= 'Credenciales incorrectas'
                return  render_template('login.html', error = msj), 401
        else:
            return render_template('login.html')
        

    @app.route('/inicio', methods=['GET', 'POST'])
    def inicio():
        return render_template('index.html')

    @app.route('/registrarPartido', methods=['GET', 'POST'])
    def registrar_Partido():
        print("Inicio Registro...")
        if request.method == 'POST':
                eq1 = request.form['equipo1']
                eq2 = request.form['equipo2']
                fecha = request.form['fecha']
                if (eq1 != None and eq1 != '')  and (eq2 != None and eq2 != '') and (fecha != None and fecha != ''):
                    print("Variables Válidas...")
                    try:
                        print("Registrando Partido...")
                        # Obtener una conexión
                        with pgdb.get_cursor() as cursor:
                            sql = f"INSERT INTO partidos (EQUIPO1, EQUIPO2, FECHA) VALUES ('{eq1}', '{eq2}', '{fecha}');"
                            print(sql)
                            cursor.execute(sql)
                            print("Partido Registrado!")
                        return  render_template('registrarPartido.html', mensaje= "el partido se registró correctamente"), 200
                    except Exception as e:
                        print("Error:", e)                  
                else:
                    if eq1 == None or eq1 == '':
                        raise ExcepcionNombreEquipo(f"Error al dar de alta el Partido con el Equipo : ={eq1}. No puede ser nulo o vacio")
                    elif eq2 == None or eq2 == '':
                        raise ExcepcionNombreEquipo(f"Error al dar de alta el Partido con el Equipo : ={eq2}. No puede ser nulo o vacio")
                    elif fecha == None or fecha == '':
                        raise fechaException(f"Error al dar de alta el Partido con Fecha : ={fecha}. No puede ser nula o vacia")
                    
        
        else:
            return render_template('registrarPartido.html')

    @app.route('/registrarLiga', methods=['GET', 'POST'])
    def registrar_Liga():
        if request.method == 'POST':
                eq1 = request.form['equipo1']
                eq2 = request.form['equipo2']
                if (eq1 != None and eq1 != '') and  (eq2 != None and eq2 != ''):
                    try:
                        # Obtener una conexión
                        with pgdb.get_cursor() as cursor:
                            sql = f"INSERT INTO ligas (EQUIPO1, EQUIPO2) VALUES ('{eq1}', '{eq2}');"
                            print(sql)
                            cursor.execute(sql)
                            print("Liga Registrada!")  
                        return  render_template('registrarLiga.html', mensaje= "La Liga se dio de alta correctamente"), 200
                    except Exception as e:
                            print("Error:", e)
                else:
                    if eq1 == None or eq1 == '':
                        raise ExcepcionNombreEquipo(f"Error al dar de alta el Partido con el Equipo : ={eq1}. No puede ser nulo o vacio")
                    elif eq2 == None or eq2 == '':
                        raise ExcepcionNombreEquipo(f"Error al dar de alta el Partido con el Equipo : ={eq2}. No puede ser nulo o vacio")
        else:
            return render_template('registrarLiga.html')

    @app.route('/consultar_Ligas', methods=['GET', 'POST'])
    def mostrarLigas():
        resultados  = []
        try:
            # Obtener una conexión
            with pgdb.get_cursor() as cursor:
                # Ejecutar una consulta
                cursor.execute("SELECT * FROM ligas")
                # Obtener los resultados
                filas = cursor.fetchall()
                # Mostrar los resultados
                for fila in filas:
                    print(fila)
                    resultados.append(fila) 
        except Exception as e:
            print("Error:", e)
        return render_template("ligas.html", datos=resultados)

    @app.route('/consultar_Partidos', methods=['GET', 'POST'])
    def mostrarPartidos():
        resultados  = []
        try:
            # Obtener una conexión
            with pgdb.get_cursor() as cursor:
                # Ejecutar una consulta
                cursor.execute("SELECT * FROM partidos")
                # Obtener los resultados
                filas = cursor.fetchall()
                # Mostrar los resultados
                for fila in filas:
                    print(fila)
                    resultados.append(fila) 
        except Exception as e:
            print("Error:", e)
        return render_template("partidos.html", datos=resultados), 200

    #-----------------------Equipos-------------------------------
    #-------------------------------------------------------------
    @app.route('/registrarEquipo', methods=['GET', 'POST'])
    def registrarEquipo():
        if request.method == 'POST':
                nombre = request.form['nombre']
                print("Nombre de Equipo...", nombre)
                if (nombre != None and nombre != ''):
                    try:
                        # Obtener una conexión
                        with pgdb.get_cursor() as cursor:
                            sql = f"INSERT INTO equipos (NOMBRE) VALUES ('{nombre}');"
                            print(sql)
                            cursor.execute(sql)
                            print("Equipo Registrado!")
                        return  render_template('registrarEquipo.html', mensaje= "el equipo se dio de alta correctamente"), 200
                    except Exception as e:
                        print("Error:", e)                        
                else:
                    raise ExcepcionNombreEquipo(f"Error al dar de alta el Equipo: Nombre={nombre}. El nombre NO puede ser Vacío o NULO")
        else:
            return render_template('registrarEquipo.html')


    @app.route('/consultar_equipos', methods=['GET', 'POST'])
    def mostrarEquipos():
        resultados  = []
        try:
            # Obtener una conexión
            with pgdb.get_cursor() as cursor:
                # Ejecutar una consulta
                cursor.execute("SELECT * FROM equipos")
                # Obtener los resultados
                filas = cursor.fetchall()
                # Mostrar los resultados
                for fila in filas:
                    print(fila)
                    resultados.append(fila) 
        except Exception as e:
            print("Error:", e)
        return render_template("equipos.html", datos=resultados)


    @app.route('/registrarJugador', methods=['GET', 'POST'])
    def registrarJugador():
        if request.method == 'POST':
                nombre = request.form['nombre']
                apPaterno = request.form['apPaterno']
                apMaterno = request.form['apMaterno']
                if (nombre != None and nombre != '')  and (apPaterno != None and apPaterno != '') and (apMaterno != None and apMaterno != ''):
                    try:
                        # Obtener una conexión
                        with pgdb.get_cursor() as cursor:
                            sql = f"INSERT INTO jugadores (NOMBRE, APPATERNO, APMATERNO) VALUES ('{nombre}','{apPaterno}', '{apMaterno}');"
                            print(sql)
                            cursor.execute(sql)        
                        return  render_template('registrarJugador.html', mensaje= "el jugador se dio de alta correctamente"), 200

                    except Exception as e:
                        print("Error:", e)
                else:
                    if nombre == None or nombre == '':
                        raise ExcepcionJugador(f"Error al dar de alta el Jugador con el Nombre : ={nombre}. No puede ser nulo o vacio")
                    elif apPaterno == None or apPaterno == '':
                        raise ExcepcionJugador(f"Error al dar de alta el Jugador con el Equipo : ={apPaterno}. No puede ser nulo o vacio")
                    elif apMaterno == None or apMaterno == '':
                        raise ExcepcionJugador(f"Error al dar de alta el Jugador con el Equipo : ={apMaterno}. No puede ser nulo o vacio")                  
        else:
            return render_template('registrarJugador.html')

    @app.route('/consultar_jugadores', methods=['GET', 'POST'])
    def mostrarJugadores():
        resultados  = []
        try:
            # Obtener una conexión
            with pgdb.get_cursor() as cursor:
                # Ejecutar una consulta
                cursor.execute("SELECT * FROM jugadores")
                # Obtener los resultados
                filas = cursor.fetchall()
                # Mostrar los resultados
                for fila in filas:
                    print(fila)
                    resultados.append(fila) 
        except Exception as e:
            print("Error:", e)
        return render_template("jugadores.html", datos=resultados)


    #-----------Entrenador---------------------------------------------

    @app.route('/registrarEntrenador', methods=['GET', 'POST'])
    def asignar_Entrenador():
        if request.method == 'POST':
                nombre = request.form['nombre']
                apPaterno = request.form['apPaterno']
                apMaterno = request.form['apMaterno']
                if (nombre != None and nombre != '')  and (apPaterno != None and apPaterno != '') and (apMaterno != None and apMaterno != ''):
                    try:
                        # Obtener una conexión
                        with pgdb.get_cursor() as cursor:
                            sql = f"INSERT INTO entrenadores (NOMBRE, APPATERNO, APMATERNO) VALUES ('{nombre}','{apPaterno}', '{apMaterno}');"
                            print(sql)
                            cursor.execute(sql)        
                        return  render_template('asignarEntrenador.html', mensaje= "el entrenador se dio de alta correctamente"), 200

                    except Exception as e:
                        print("Error:", e)
                else:
                    if nombre == None or nombre == '':
                        raise ExcepcionJugador(f"Error al dar de alta el Jugador con el Nombre : ={nombre}. No puede ser nulo o vacio")
                    elif apPaterno == None or apPaterno == '':
                        raise ExcepcionJugador(f"Error al dar de alta el Jugador con el Equipo : ={apPaterno}. No puede ser nulo o vacio")
                    elif apMaterno == None or apMaterno == '':
                        raise ExcepcionJugador(f"Error al dar de alta el Jugador con el Equipo : ={apMaterno}. No puede ser nulo o vacio") 
        else:
            return render_template('asignarEntrenador.html')

    @app.route('/consultar_entrenadores', methods=['GET', 'POST'])
    def mostrarEntrenadores():
        resultados  = []
        try:
            # Obtener una conexión
            with pgdb.get_cursor() as cursor:
                # Ejecutar una consulta
                cursor.execute("SELECT * FROM entrenadores")
                # Obtener los resultados
                filas = cursor.fetchall()
                # Mostrar los resultados
                for fila in filas:
                    print(fila)
                    resultados.append(fila) 
        except Exception as e:
            print("Error:", e)
        return render_template("entrenadores.html", datos=resultados)

    @app.route('/reglamento')
    def mostrarReglamento():
        return render_template('reglamento.html')


def crearApp():
    app = Flask(__name__)
    registrarRutas(app)
    return app

app = crearApp()
pgdb = PostgresDB()
pgdb.init_app(app)
pgdb.create_all_tables()

if __name__ == "__main__":
    app.run(debug=True)