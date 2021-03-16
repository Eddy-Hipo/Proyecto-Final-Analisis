# Pulso politico por provincias de Ecuador.
## 1. Arquitectura
![alt text](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/2_PulsoPoliticoProvincias/DataLake_ProvinciasEC.png)
## 2. Scripts de extracción, filtrado y exportación de datos
### - Script 1 - Logstash
#### _(BaseCandidatos.csv)_ 
El archivo representa la base de datos sin trabajar para este tema.
### - Script 2 - Tweppy
#### _(lasso.py)_
Usando codigo y librerias de python como tweppy y la base de datos couchdb (lasso.db) se recopilaron tweets desde el 4 al 8 de marzo del presente año, los mismos que esten a favor de lasso. Usando como palabra clave lasso.
### - Script 3 - Facebook Scraper
#### _(yaku.py)_
Usando codigo y librerias de python como tweppy y la base de datos couchdb (yaku.db) se recopilaron tweets desde el 4 al 8 de marzo del presente año, los mismos que esten a favor de yaku. Usando como palabra clave pachakutik.
### - Script 4 - Exportación a .csv
#### _(candidatos.csv)_ _(proyecto.csv)_ 
Se leyeron todos los registros de couch y se los paso a un csv denominado proyecto, donde se juntan ambas bases de datos.
### - Script 5 - Elasticsearch
#### _(mapping)_ 
El archivo contiene el código de mapeo utilizando para trabajar con el csv denominado proyecto en elasticsearch al momento de crear el indice denominado proyecto al igual que el archivo.
### - Script 6 - Logstash
#### _(logstash.conf)_ 
El archivo contiene el código de logstash para la lectura y escritura de un csv a elasticsearch levantado localmente.
## 3. Visualizaciones y análisis
Es importante resaltar que el archivo csv contiene información de dos temporadas (1. La temporada antes de las votaciones y 2. La temporada de la presentación definitivia de los resultados.).
### - Con Kibana
#### Promedio de likes por provincias
![Kibana1](https://user-images.githubusercontent.com/66123679/111061340-dc2be580-8470-11eb-800c-9f5901bbb643.PNG)<br/>
**Análisis:** Es de conocimiento general que durante los dias proximos a las votaciones el candidato postulante tiene derecho a realizar su campaña donde se espera ganar el apoyo de las personas en las diferentes provincias, es por esto que en unas provincias el candidato puede recibir mas acogida que en otras. Como vemos en la grafica el candidato Lasso tiene una gran aceptación en algunas provincias que el candidato yaku. </br>
#### Promedio de likes y retweets por fecha
![Kibana2](https://user-images.githubusercontent.com/66123679/111061663-822c1f80-8472-11eb-83b6-a34f9806b3d8.PNG) <br/>
**Análisis:** En la grafica de barras se puede apreciar como influye mucho la epoca en la que se recopilan datos pues como vemos para algunos candidatos como en este caso Guillermo Lasso quien tuvo una mayor actividad el lunes 1 de Febreo a diferencia del candidato Yaku Peréz, sin embargo en el periodo de 4 al 8 de marzo su presencia en twitter disminuye, a pesar de eso lasso supera a yaku tanto en likes como retweets</br>
#### Publicaciones por fecha y ubicación
![Kibana3](https://user-images.githubusercontent.com/66123679/111061567-05994100-8472-11eb-99c0-dee49db4bfa7.PNG) <br/>
**Análisis:** La grafica indica la actividad a favor de cada candidato considerando la fecha, se puede ver como Lasso supera en las 5 provincias mas significativas en este analisis que son El oro, Azuay, Cañar, Cotopaxi, Guayas. Lo sorprendente es que en las otras provincias la presencia de yaku se hace mas notoria.</br>
### - Con Tableau
#### Mapa de resultados
 ![Tableau1](https://user-images.githubusercontent.com/66123679/111060511-696c3b80-846b-11eb-894d-3f7bb97aee07.PNG)<br/>
**Análisis:** El mapa permite un mayor acercamiento a las provincias con mayor actividad como tweets, likes, retweets siendo la gran mayoria a favor de Guillermo lasso  </br>
En conclusion a pesar de que la temporada de votaciones siga parcialmente abierta se puede notar una disminución en las redes como Twitter, no obstante a pesar de ser una temporada baja para la politica el candidato Guillermo Lasso ha logrado tener mas actividad que el candidato Yaku, lo que tiene sentido pues es él quien se estara peleando la presidencia con el ya finalista Andres Arauz.
