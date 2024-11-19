import sqlite3

class db:
    
    # def creacion_tablas():
    def __init__(self,db_name="bd.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name) #CONEXION CON LA DB
        self.cursor = self.conn.cursor() #CURSOR PARA EJECUTAR SQL
        
    def creacion_tablas(self):
        #Tabla para datos de JSON API
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS json (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                body TEXT NOT NULL,
                                userid INTEGER NOT NULL                                
                            )
                            """)
        self.conn.commit()#COMMIT DEBE IR AL FINAL DEL METODO