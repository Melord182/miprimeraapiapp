import requests
import json
class jsonapi: #Metodo get y post (CRUD JSONAPI)
    
    def __init__(self, url_inicial):
        self.url_inicial = url_inicial
        
    def obtener_datos_get(self, pagina):
        url = f"{self.url_inicial}/{pagina}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            print("Datos obtenidos con GET")
        
            for datos in data:
                print (f"Tarea {datos['id']}",f"{datos['title']}\n".capitalize())        
                
            return data

    def guardar_datos_post(self,pagina,datos):
        url = f"{self.url_inicial}/{pagina}"
        response = requests.post(url, json=datos)
        
        if response.status_code==201:
            print("Datos enviados con POST:")
            print(json.dumps(response.json(), indent = 4))
            
        else:
            print("Error al enviar datos:", response.status_code)
            return None
        
    
    def modificar_datos_put(self,pagina,datos,id):
        url = f"{self.url_inicial}/{pagina}/{id}"
        response = requests.put(url, json=datos)
        
      
        print("Datos modificados con PUT:")
        print(json.dumps(response.json(), indent=5))

    def eliminar_datos_delete(self,id):
        url= f"{self.url_inicial}/posts/{id}"
        response = requests.delete(url)
        print (f"Tarea eliminada")
        print(json.dumps(response.json()))



    
if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"
    cliente = jsonapi(api_url)

