
import requests
from bs4 import BeautifulSoup

encabezado = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/79.0.3945.117 Safari/537.36"
}

# url semilla
url="https://stackoverflow.com/"


resp = requests.get(url, headers=encabezado)


sopa = BeautifulSoup(resp.text, features="lxml")

contenedor_de_preguntas = sopa.find(id="question-mini-list")
print(contenedor_de_preguntas)
