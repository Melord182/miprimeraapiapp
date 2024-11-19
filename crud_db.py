import sqlite3
from crud_api import *
from db import *

class jsonapidb(db):
    def __init__(self, db_name="bd.db"):
        super().__init__(db_name)
    
    def obtener_datos_db(self):
        cursor = self.conn.execute("""
                          SELECT * FROM json ORDER BY id 
                          """)
        data = cursor.fetchall()
        return data
    
    def guardar_datos_db(self,title,body,userId):
        
        self.conn.execute("""
                          INSERT INTO json (title, body, userId) VALUES (?,?,?)
                          """, (title,body,userId))
        self.conn.commit()
        
    def modificar_datos_db(self,id,title,body,userId):
        
        self.conn.execute("""
                          UPDATE json SET
                          title = ?,
                          body = ?,
                          userId = ?
                          WHERE id = ?
                          """,(title,body,userId,id))
        self.conn.commit()
    
    def eliminar_datos_db(self,id):
        
        self.conn.execute(""" 
                          DELETE FROM json
                          WHERE id = ?
                          """,(id,))
        self.conn.commit()