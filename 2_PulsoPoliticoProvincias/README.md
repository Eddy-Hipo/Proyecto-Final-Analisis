# Pulso politico por provincias de Ecuador.
## 1. Arquitectura
![alt text](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/2_PulsoPoliticoProvincias/DataLake_Provincias.png)
## 2. Scripts de extracción, filtrado y exportación de datos
### - Script 1 - Tweppy
#### _(lasso.py)_
Usando codigo y librerias de python como tweppy y la base de datos couchdb (lasso.db) se recopilaron tweets desde el 4 al 8 de marzo del presente año, los mismos que esten a favor de lasso. Usando como palabra clave lasso.
### - Script 2 - Facebook Scraper
#### _(yaku.py)_
Usando codigo y librerias de python como tweppy y la base de datos couchdb (yaku.db) se recopilaron tweets desde el 4 al 8 de marzo del presente año, los mismos que esten a favor de yaku. Usando como palabra clave pachakutik.
### - Script 3 - Exportación a .csv
#### _(candidatos.csv)_ _(proyecto.csv)_ 
Se leyeron todos los registros de couch y se los paso a un csv denominado proyecto, donde se juntan ambas bases de datos.
### - Script 4 - Elasticsearch
#### _(mapping)_ 
El archivo contiene el código de mapeo utilizando para trabajar con el csv denominado proyecto en elasticsearch al momento de crear el indice denominado proyecto al igual que el archivo.
### - Script 5 - Logstash
#### _(logstash.conf)_ 
El archivo contiene el código de logstash para la lectura y escritura de un csv a elasticsearch levantado localmente.
## 3. Visualizaciones y análisis
Es importante resaltar que el archivo csv contiene información de dos temporadas (1. La temporada antes de las votaciones y 2. La temporada de la presentación definitivia de los resultados.).
### - Con Kibana
#### Grafica de barras por retweets
![Kibana1](https://user-images.githubusercontent.com/66123679/111060487-3629ac80-846b-11eb-8226-dd8b5bcc49c8.PNG)
<br/>
**Análisis:** En la grafica se puede visualizar como la temporada que se antepone a las votaciones, ambs candidatos tienen un algo porcentaje de retweets. Sin embargo dicho porcentaje se decae en la temporada actual pues considerando las dos fechas dominantes del 4 al 8 de marzo se ve un decremento del porcentaje, no obstante, el candidato Lasso sigue por delante del candidado yaku.</br>
#### Visualización por fechas
![Kibana2](https://user-images.githubusercontent.com/66123679/111060502-56f20200-846b-11eb-968e-bbf86081820f.PNG)
<br/>
**Análisis:** En la grafica se puede apreciar mejor la gran diferencia entre ambos candidatos consdierando la fecha pues Guillermo lasso a pesar de la temporada sigue con alto record de tweets, lo contrario ocurre con yaku pues su popularidad disminuye por las epocas.</br>
#### Las provincias con mas likes 
![Kibana3](https://user-images.githubusercontent.com/66123679/111060503-5bb6b600-846b-11eb-83d0-3e9005e5b24f.PNG)
<br/>
**Análisis:** Es de conocimiento general que durante los dias proximos a las votaciones el candidato postulante tiene derecho a realizar su campaña donde se espera ganar el apoyo de las personas en las diferentes provincias, es por esto que en unas provincias el candidato puede recibir mas acogida que en otras. Como vemos en la grafica el candidato Lasso tiene una gran aceptación en algunas provincias que el candidato yaku. </br>
#### Maximo numero de likes y retweets por candidatos
![Kibana4](https://user-images.githubusercontent.com/66123679/111060505-61140080-846b-11eb-96ae-c200d453304f.PNG)
<br/>
**Análisis:** En la grafica se puede aprecias como el candidato lasso tiene una gran ventaja sobre el candidato yaku tanto en likes como en retweets </br>
#### Promedio de las publicaciones por ubicación
![Kibana5](https://user-images.githubusercontent.com/66123679/111060509-65401e00-846b-11eb-9d4e-591a62ba0c19.PNG)
<br/>
**Análisis:** La grafica de pastel se puede apreciar con mas detenimiento las provincias mas representativas como son Pichincha, Guayaquil, Orellana, Tungurahua y las otras siendo Guayaquil/Guayas la provincia donde se ha dado mas publicaciones. </br>
### - Con Tableau
#### Mapa de resultados
 ![Tableau1](https://user-images.githubusercontent.com/66123679/111060511-696c3b80-846b-11eb-894d-3f7bb97aee07.PNG)<br/>
**Análisis:** El mapa permite un mayor acercamiento a las provincias con mayor actividad como tweets, likes, retweets siendo la gran mayoria a favor de Guillermo lasso  </br>
En conclusion a pesar de que la temporada de votaciones siga parcialmente abierta se puede notar una disminución en las redes como Twitter, no obstante a pesar de ser una temporada baja para la politica el candidato Guillermo Lasso ha logrado tener mas actividad que el candidato Yaku, lo que tiene sentido pues es él quien se estara peleando la presidencia con el ya finalista Andres Arauz.
