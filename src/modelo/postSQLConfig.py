from psycopg2.pool import ThreadedConnectionPool
from contextlib import contextmanager


db_config = { "host" : "localhost",
                "database" : "ligafutbol",
                "user" : "roberto",
                "password" : "elizabeth17"}


_tabla_jugadores = "CREATE TABLE jugadores (" \
                "id SERIAL PRIMARY KEY,"  \
                "nombre TEXT,"   \
                "apPaterno TEXT," \
                "apMaterno TEXT" \
                ");"

_tabla_entrenadores = "CREATE TABLE entrenadores (" \
                "id SERIAL PRIMARY KEY,"  \
                "nombre TEXT,"   \
                "apPaterno TEXT," \
                "apMaterno TEXT" \
                ");"

_tabla_arbitros = "CREATE TABLE arbitros (" \
                "id SERIAL PRIMARY KEY,"  \
                "nombre TEXT,"   \
                "apPaterno TEXT," \
                "apMaterno TEXT" \
                ");"

_tabla_equipos = "CREATE TABLE equipos (" \
                "id SERIAL PRIMARY KEY,"  \
                "nombre TEXT"   \
                ");"

_tabla_partidos = "CREATE TABLE partidos (" \
                "id SERIAL PRIMARY KEY,"  \
                "equipo1 TEXT,"   \
                "equipo2 TEXT," \
                "fecha TEXT" \
                ");"

_tabla_ligas = "CREATE TABLE ligas (" \
                "id SERIAL PRIMARY KEY,"  \
                "equipo1 TEXT,"   \
                "equipo2 TEXT" \
                ");"

class PostgresDB:
    def __init__(self):
        self.app = None
        self.pool = None

    def init_app(self, app):
        self.app = app
        self.connect()

    def connect(self):
        self.pool = ThreadedConnectionPool(minconn=1, maxconn=30, **db_config)

    def create_all_tables(self):
        drop_jugadores ="DROP TABLE IF EXISTS jugadores;"
        drop_entrenadores ="DROP TABLE IF EXISTS entrenadores;"
        drop_arbitros ="DROP TABLE IF EXISTS arbitros;"
        drop_equipos ="DROP TABLE IF EXISTS equipos;"
        drop_partidos ="DROP TABLE IF EXISTS partidos;"
        drop_ligas ="DROP TABLE IF EXISTS ligas;"

        with self.get_cursor() as cur: 
            #---------Dropear Tablas-------------
            
            cur.execute(drop_jugadores)
            cur.execute(drop_entrenadores)
            cur.execute(drop_arbitros)
            cur.execute(drop_equipos)
            cur.execute(drop_partidos)
            cur.execute(drop_ligas)
            
            #-----crear todas las tablas--------
            
            cur.execute(_tabla_jugadores)
            cur.execute(_tabla_entrenadores)
            cur.execute(_tabla_arbitros)
            cur.execute(_tabla_equipos)
            cur.execute(_tabla_partidos)
            cur.execute(_tabla_ligas)


    @contextmanager
    def get_cursor(self):
        if self.pool is None:
            self.connect()
        con = self.pool.getconn()
        try:
            yield con.cursor()
            con.commit()
        finally:
            self.pool.putconn(con)