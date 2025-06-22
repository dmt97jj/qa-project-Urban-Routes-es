José Juan Barraza Barrón, grupo 29, proyecto Sprint 8

Descripción del proyecto.
Se trabajó en la aplicación "Urban Routes", automatizando y ejecutando un total de 8 pruebas mediante solicitudes URL de tipo "Get", en el que se probaron
diferentes funciones de la aplicación, basado en la lista de comprobación, las cuales fueron:
1. Definir el punto de partida del viaje y el destino.
2. Seleccionar la tarifa "Comfort" dentro del servicio de solicitud de taxi.
3. Se introdujo un número de teléfono y se verificó mediante un codigo enviado por mensaje de texto.
4. Se agregó un nuevo metodo de pago; una tarjeta de credito/debito.
5. Se probó el escribir un mensaje de texto al conductor del taxi.
6. Una solicitud para una manta y pañuelos
7. Se agregaron 2 helados al pedido
8. Se comprobó que se desplegara la nodal con la información de la solicitud del viaje y la busqueda de un conductor.
Las 8 diferentes pruebas llevadas a cabo en la aplicación "Urban Routes" arrojaron resultados positivos, comprobando así, que la aplicación funciona de forma correcta,
pues los resultados reales concuerdan con los resultados esperados, cumpliendo así, las pruebas de forma exitosa y funcionando a la perfección.

Para realizar las pruebas, primero se copió el repositorio "qa-project-Urban-Routes-es" de la plataforma Github. Este repositorio fue guardado en una carpeta donde se almacenaron
los archivos sobre los cuales se trabajó en las pruebas. Se utilizaron dos archivos ".py" 1.-"data.py" en donde se almacenaron los datos que iban a ser utilizados para ejecutar las pruebas,
Y 2.-"main.py" en donde se hicieron dos clases: la primera "UrbanRoutesPage" en donde se introdujeron los localizadores y los métodos que iban a ser utilizados en las prueba y "TestUrbanRoutes"
en donde se ejecutaron las 8 pruebas.
Fuente de documentación: apiDOC
Para la configuración del proyecto: 
1. El lenguaje del proyecto: Pure Python
2. Ruta al proyecto: Seleccioné la ruta en la que se encontraban todos los archivos y donde había hecho el repositorio en la plataforma GitHub.
que es la siguiente: C: \users\user_name\projects\qa-project-Urban-Routes-es
3. Seleccioné "Virtualenv" como Entorno virtual
4. Seleccioné la ruta al interprete de Python que había instalado previamente.

Importé las librerias al archivo "main.py" que iban a ser utilizadas para que las pruebas puedan funcionar, las cuales fueron: 
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

Agregando tambien, la importación del archivo "data.py" para poder hacer uso de los datos que iban a introducirse en las pruebas.
Por último se instaló y se importó Pytest, para poder ejecutar todas las pruebas de una forma automatizada.

Para poder ejecutar las pruebas de forma correcta, una vez que esté instalado Pytest y la librería haya sido importada al documento "main.py" donde se escribieron
las pruebas, y confirmar que el URL almacenado en "urban_routes_url" sea válido, basta con hacer click en la flecha verde al costado izquierdo de la linea de cada una de las pruebas, para ejecutarlas de forma individual o bien, ejecutarlas desde la clase "TestUrbanRoutes"
ya que esta, ejecutará las 8 pruebas al mismo tiempo, o bien, escribien directamente en la consola a la cual se puede acceder mediante el panel inferior izquierdo o con el atajo "alt+F12".
