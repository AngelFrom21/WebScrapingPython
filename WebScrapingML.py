import requests as req
from bs4 import BeautifulSoup as bs

url = 'https://listado.mercadolibre.com.mx/maison-alhambra#D[A:maison%20alhambra]'

respuesta = req.get(url)
nombres_L = []
precios_L = []
if respuesta.status_code == 200:
  soup = bs(respuesta.text,'html.parser')

  #objetivos
  #nombre de los productos
  nombres = soup.find_all('a',class_='poly-component__title')
  #vendedores
  vendedores = soup.find_all('span', class_ = 'poly-component__seller')
  #precios:
  #precios = soup.find_all('span', class_ = 'price-tag-fraction')
  precios = soup.find_all('span',class_ = 'andes-money-amount__fraction')

  #impresiones
  for i in nombres:
    #print(i.text)
    nombres_L.append(i.text)
  for j in precios:
    j = j.text.replace(',','')
    j = int(j)
    if j<150:
      pass
    else:
      precios_L.append(j)
  print(len(precios_L))
  print(len(nombres_L))
  for i in nombres_L:
    print(i)
  print(precios_L)
else:
  print('error', f'estado: {respuesta.status_code}')