#Ejemplo de POST
import requests

url = "https://jsonplaceholder.typicode.com/posts"
usuario = {
    "title": "Título",
    "body": "El cuerpo",
}
respuesta = requests.post(url, json=usuario)
# Ahora decodificamos la respuesta como json
como_json = respuesta.json()
print("La respuesta del servidor es:")
print(como_json)
# Podemos acceder al id por ejemplo
id = como_json["id"]
print(f"El id es: {id}")