# Pulso politico por ciudades de Ecuador.
## 1. Arquitectura
![alt text](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/1_PulsoPoliticoCiudades/DataLake_CiudadesEC.png)
## 2. Scripts de extracción, filtrado y exportación de datos
### - Script 1 - Tweppy
#### _(arauz.py)_
Al utilizar el codigo que contiene librerias de python como tweppy y la base de datos mongoDB la cual nose permite exportar la base de datos en un archivo JSON o CSV (Ciudades.csv), se recopilaron tweets desde el 4 al 8 de marzo del presente año, los mismos que muestran opinión acerca del candidato Arauz. Usando como filtro la ubicación con la ayuda de las coordenadas en formato csv obtenidas con Bounding Box, adicionalmente se filtro la palabra clave arauz. 
### - Script 2 - Datos de Mongo a Elasticsearch 
#### _(Recopilacion y almacenamiento de datos/MongoDB_to_ElasticSearch_NodeJS)_ 
Se utilizo el siguiente proyecto en el que se recopilan los datos de determinada collección en MongoDb y son enviados a ElasticSearch el proceso detallado esta en el README del proyecto.

## 3. Visualizaciones y análisis
Como la data ha sido enviada directo desde MongoDB via Node.js a ElasticSearch se procedio a mapear los datos en la herramienta Power Bi donde se cargo el archivo csv que nos proporciono MongoDB. 
En este sentido se va trabajar con los siguientes datos del tweet: Fecha de creación, menciones, nombre de usuario, el texto del tweet, el nombre de la ciudad, la locación del usuario y los hashtags.  

### - Con Kibana
#### Principales Hashtags en los tweets
![Kibana1](https://user-images.githubusercontent.com/66123679/111061340-dc2be580-8470-11eb-800c-9f5901bbb643.PNG)<br/>
**Análisis:** La opinión que tienen cierta parte de la población del Ecuador en torno al candidato Andrés Arauz es evidente, los principales hashtags encontrados son: Comparte: este hashtag es usado como muestra de apoyo hacia el candidato, AruazEsCorrea y RevoluciónCiudadana: indican que es de conocimiento publico que la ciudadnia que voto por él es porque le dan la confianza que tenian a dicho partido político. </br>
#### Menciones de los usuarios
![Kibana2](https://user-images.githubusercontent.com/66123679/111061663-822c1f80-8472-11eb-83b6-a34f9806b3d8.PNG) <br/>
**Análisis:** En la gráfica de dona se puede apreciar que principalmente los usuarios de Twitter mencionan al candidato Andréz Arauz y a Rafael Correa, pues el movimiento político Compromiso Social RC5 mantiene los ideales de la Revolución Ciudadana que en su momento defendio el expresidente Rafael Correa</br>
#### Tweets por ciudad 
![Kibana3](https://user-images.githubusercontent.com/66123679/111061567-05994100-8472-11eb-99c0-dee49db4bfa7.PNG) <br/>
**Análisis:** La gráfica de barras nos indica las ciudades que estan tuiteando el tema de arauz en el intervalo de tiemo que se recopiló los tweets, las ciudades que destacan son: Quito, Guayaquil, Portoviendo y Manta. Existen varias ciudades de la región costa que tambien han tuiteado pero no alcanzan un número considerable. Cuando se inice la campaña electoral puede que estos datos cambien. </br>
### - Con Tableau
#### Mapa de resultados
 ![Tableau1](https://user-images.githubusercontent.com/66123679/111060511-696c3b80-846b-11eb-894d-3f7bb97aee07.PNG)<br/>
**Análisis:** El mapa generado con la herramienta de Power Bi nos permite observar de manera general como a lo largo del Ecuador principalmente en las ciudades de la región Costa se esta hablando sobre el candidato a presidnete Andrés Arauz.</br>
En conclusion los datos recopilados nos permiten tener una idea un poco clara de como ven los ciudadanos al candidato presidenciable Andrés Arauz es evidente que el pueblo es conciente de que representa al partido político del expresidente Rafael Correa, la ciudadania ha visto esto como una posible salida a la situación actual del país pero es necesario analizar a fondo a los candidatos, la intención de voto puede cambiar con el inicio de la campaña electoral y el debate que tendra lugar el 21 de marzo.
