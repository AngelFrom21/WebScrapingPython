# WebScrapingPython
Este repositorio contiene proyectos con un enfoque en extracción de datos de páginas web usando librerias de python como BeautifulSoup y Requests

<h1 align = "left">Motivación</h1>

El monitoreo de precios de productos en distintas plataformas de e-commerce permite al usuario<br>
ya sea consumidor o proveedor estimar el mejor lugar de compra/venta así como la plataforma de<br>
a lo largo de una ventana de tiempo determinada, que puede ser presente o pasada.<br>
Con los datos que recopila este scraper es posible determinar tendencias de compra y venta<br>
a lo largo de un año para así establecer estrategias de acuerdo a los comportamientos obervados.

<h3 align = 'left'>Propuesta</h3>

Los archivos de código presentes en este repositorio (Extractor ML, AMZ, LVP) envian una solicitud de acceso<br>
a los servidores de las plataformas de e-commerce con la siguiente información:<br>

- <b>Mercado Libre:</b><br>
    La página no requiere uso de algun agente o cookies, basta enviar la solicitud de página
- <b>Amazon:</b><br>
    Se emplea un user agent junto con la cookie que identifica la sesión, de otra forma el servidor<br>
    bloquea la consulta.
- <b>Liverpool:</b><br>
    Al igual que amazon se emplea un user agent junto con la cookie que identifica la sesión, de otra forma el servidor<br>
    bloquea la consulta.<br>
    
Estos archivos, mediante las librerias Requests y BS4 junto con las etiquetas HTML de precio, vendedor (si existe) y fecha<br>
extraen los valores antes mencionados y los convierten a formatos convenientes para su visualización y análisis.

<h3>Resultados</h3>

Los resultados de cada consulta se exportan de momento en formato csv, para su posterior manipulación en pandas

<h3>Futuras actualizaciones</h3>

- incorporación de Streamlit para visualizar datos de forma interactiva.
- exportación a más formatos como sql, xlsx etc
- incorporar user input para la página de la plataforma.
