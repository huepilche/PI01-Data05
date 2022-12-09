# Proyecto de 'Data Engineering' ETL-API desarrollado como contenedor de Docker 

BREVE DESCRIPCION:

Se realiza un proceso de Extracción, Transformación y Carga con librería PANDAS, para posteriormente consumir la Base de Datos generada a través de una FastAPI encapsulada en un Docker. El obejtivo es realizar consultas a una base de datos de producciones cinematográficas como un servicio de interfaz Web.

HERRAMIENTAS:

Pandas y Sqlalchemy: Usado para el procesamiento y creación de Base de Datos

FastAPI: Usado para implementar aplicación de interfaz web que genera consultas a la Base de Datos

Docker: usado para crear imagen de FastAPI en contenedor


CONTENIDO DEL REPOSITORIO: En la carpeta principal se encuentra el archivo Docker junto a sus requerimientos y la licencia de uso, Un archivo .ipynb que contiene la ingesta, normalización y transformación de los datos. En la carpeta 'Datasets' se encuentran los archivos .csv y .json que contienen la información de las  producciones cinem  y  un archivo .db asociado a la base de datos correspondiente. Finalmente, en la carpeta App  encontramos un archivo .py con el código para la implementación de la la FastAPI.

CONSULTAS:

Se consideran cuatro funciones que entregan la siguiente informació

1) Película o programa de TV de mayor duración, en minutos o n° de temporadas respectivamente de una plataforma determinada. Comando asociado 'get_max_duration' con parámetros 'year', 'plataforma' y 'tipo'.
2) Cantidad de Películas y programas de TV de cada plataforma. Comando asociado 'get_count_platform' con parámetro 'plataforma'
3) Cantidad de Películas y programas de TV de un determinado género para cada plataforoma. Comando asociado 'get_listedin' con parámetro 'genero'.
4) Actor con el mayor número de participaciones en producciones para una determinada plataforma y año. Comando asociado 'get_actor' con parámetros 'year' y 'plataforma'
 
'year': año de lanzamiento
'plataforma': Amazon, Disney, Hulu o Netflix
'tipo': Movie o TVShow
'genero': género de la producción cinematográfica por ejemplo Drama, Comedy, Horror, etc.
