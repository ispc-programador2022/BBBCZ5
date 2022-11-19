import pandas as pd # libreria manipulacion de datos
import seaborn as sns # Libreria graficas
import requests
from bs4 import BeautifulSoup
#página seleccionada para realizar scraping
url = "https://www.worldometers.info/world-population/population-by-country/"

#Obtener un requests de la url
r = requests.get(url)

#preparar la sopa
soup = BeautifulSoup(r.content, 'html.parser')

#Traer tabla
rows = soup.find('table', attrs={"id":"example2"}).find('tbody').find_all('tr')


#Traer los datos a cada lista
pais = []
poblacion = []
cambio_anual = []
cambio_neto = []
densidad = []
superficie = []
migrantes = []
pobl_urbana = []
for row in rows:
  pais.append(row.find_all('td')[1].get_text())
  poblacion.append(row.find_all('td')[2].get_text())
  cambio_anual.append(row.find_all('td')[3].get_text())
  cambio_neto.append(row.find_all('td')[4].get_text())
  densidad.append(row.find_all('td')[5].get_text())
  superficie.append(row.find_all('td')[6].get_text())
  migrantes.append(row.find_all('td')[7].get_text())
  pobl_urbana.append(row.find_all('td')[10].get_text())


  #DataFrame
df = pd.DataFrame({"País":pais, "Poblacion":poblacion, "Cambio Anual":cambio_anual, "Cambio Neto":cambio_neto, "Densidad (P/Km2)":densidad, "Superficie (Km2)":superficie, "Migrantes":migrantes, "Población Urbana":pobl_urbana})

#imprimir df
df

#descargar el csv
df.to_csv('poblacion.csv', index=False, encoding='utf-8')
