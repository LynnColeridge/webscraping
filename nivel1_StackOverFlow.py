import requests
from bs4 import BeautifulSoup

encabezado = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/79.0.3945.117 Safari/537.36"
}

# url semilla
# url="https://stackoverflow.com/"
url_2 = "https://stackoverflow.com/questions"

# resp = requests.get(url, headers=encabezado)
r = requests.get(url_2, headers=encabezado)

# sopa = BeautifulSoup(resp.text, features="lxml")
s = BeautifulSoup(r.text, features="lxml")

# busca el tag div que tenga el id "questions"
contenedor_de_preguntas = s.find("div", id="questions")

# dentro del div anterior, busca los divs que tengan la clase question summary
lista_de_preguntas = contenedor_de_preguntas.find_all("div", class_="question-summary")
print(lista_de_preguntas)