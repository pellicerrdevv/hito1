from cliente import APIClient
from procesador import procesar_usuario
from dotenv import load_dotenv
import os, json

if __name__ == "__main__":

    load_dotenv()
    token = os.environ.get("TOKEN")
    usuario = os.environ.get("USUARIO")
    base_url = os.environ.get("BASE_URL")

    cliente = APIClient(base_url,token)
    datos = cliente.get(f"/users/{usuario}")

    resultado = procesar_usuario(datos)

    with open("resultado.json", "w") as f:
        json.dump(resultado, f, indent = 4)

