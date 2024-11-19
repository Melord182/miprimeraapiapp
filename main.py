import sqlite3
import json
import requests
from db import *
from crud_db import jsonapidb
from crud_api import *

api_url = "https://jsonplaceholder.typicode.com"
cliente = jsonapi(api_url)


bd_cliente =  jsonapidb()
bd_cliente.creacion_tablas()







class menu_json_api:
    
    @staticmethod #ESTO ES PARA QUE PUEDAN SER LLAMDOS SIN NECESIDAD DE CREAR UN OBJETO DE LA CLASE
    def solicitar_datos_put():
        print("Crear un nuevo post")
        id = input("Que tarea desea modificar (ID): ")
        title = input("Ingrese el título del post: ")
        body = input("Ingrese el cuerpo del post: ")
        userId = input ("Ingrese el ID del autor: ")
        
        nuevo_post = {
            "id" : int(id),
            "title" : title,
            "body" : body,
            "userId" : int(userId)
        }
        return nuevo_post, title, body, userId, id
    @staticmethod
    def solicitar_datos_post():
        print("Crear un nuevo post")
        title = input("Ingrese el título del post: ")
        body = input("Ingrese el cuerpo del post: ")
        userId = input ("Ingrese el ID del autor: ")
        
        nuevo_post = {
            "title" : title,
            "body" : body,
            "userId" : int(userId)
        }
        return nuevo_post, title, body, userId


while True:
    print("""
            Bienvenido a la JSON API 
            ¿Que desea hacer?
            
            [1] Obtener datos GET
            [2] Ingresar datos POST
            [3] Modificar datos PUT
            [4] Eliminar datos DELETE
            [5] Eliminar todos los registros
            [7] Salir
            """)

    opcion = input("Opcion: ")
    if opcion == "1":
    
        cliente.obtener_datos_get("posts")
        
        print("Tareas creadas por el usuario: ")
        tareas = bd_cliente.obtener_datos_db()
        
        if tareas:
            for tarea in tareas:
                print(f"""
                    id: {tarea[0]},
                    title: {tarea[1]},
                    body: {tarea[2]},
                    userId: {tarea[3]}
                    """)
        else: print("No hay tareas guaradas en la base de datos.")
        

    elif opcion == "2":
        nuevo_post, title, body, userId = menu_json_api.solicitar_datos_post()
        
        cliente.guardar_datos_post("posts", nuevo_post)
        
        bd_cliente.guardar_datos_db(title,body,userId)

    elif opcion == "3":
        
        nuevo_post, title, body, userId, id = menu_json_api.solicitar_datos_put()
        
        cliente.modificar_datos_put("posts", nuevo_post, id)
        
        bd_cliente.modificar_datos_db(id,title,body,userId)
        
    elif opcion == "4":
        
        id = input("Ingrese el ID de la tarea a eliminar: ")
        cliente.eliminar_datos_delete(id)
        bd_cliente.eliminar_datos_db(id)

    elif opcion == "5":
        confirmacion = input("¿Estas seguro de eliminar todos los registros?")
        if confirmacion.lower() == "s":
            bd_cliente.conn.execute("DELETE FROM json")
            bd_cliente.conn.commit()
            print("Todos los registros han sido eliminados de la base de datos...")
        else:
            print("Operacion cancelada.")

    elif opcion == "7":
        #Salir del programa
        
        print("Gracias por usar JSON API!")
        print("creado por jaime lopez")
        break
    
    else:
        print("Opcion no valida")