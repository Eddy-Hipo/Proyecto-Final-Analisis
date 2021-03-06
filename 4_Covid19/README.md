# El COVID-19 en el mundo.
## 1. Arquitectura
![alt text](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/4_Covid19/DataLake_COVID.png)
## 2. Scripts de extracción y filtrado de datos
### - Script 1 - [Extracción de datos](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/4_Covid19/Recopilacion%20y%20almacenamineto%20de%20datos/covid-examen2.py)
En este Script se detalla la forma de extracción de datos desde Twitter para posteriormente almacenarlos en la Base de Datos de CouchDB.
### - Script 2 - [Envio de Datos](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/4_Covid19/Recopilacion%20y%20almacenamineto%20de%20datos/logstash.conf)
En este Script se detalla la manera de extraer los datos de CouchDB mediante Logstash y transferirlos a ElastickSearch, dichos datos se utilizarán para las visualizaciones en Kibana.
## 3. Visualizaciones y análisis
### - Con Kibana
### Principales Hashtags en torno al Covid 19 
![alt text](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/4_Covid19/Visualizaciones/Hashtags_covid_19.png)

**Análisis:** Los hashtags en torno al covid 19 a nivel mundial se habla sobre una posible flexibilidad parcial en torno a las medidas y restricciones que estaban tomando las naciones del mundo en temas de protección y seguridad, pues con la distribución de la vacuna contra el covid-19 ha empezado a bajar la tensión en cuanto a la problemática, pero que pasa con las naciones que no tienen acceso fácilmente a la vacunación. Es factible flexibilizar las normas o por el contrario se deberá esperar un tiempo adecuado para no tener efectos adversos.   

### Idioma registrado en los tweets
![alt text](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/4_Covid19/Visualizaciones/Idioma_origen_covid_19.png)

**Análisis:** En la gráfica de dona se puede apreciar que principalmente el idioma con el que se han registrado los usuarios de las cuentas de Twitter que han mencionado temas referentes al covid-19 es en mayoritariamente en el idioma ingles pues en ciertas naciones como Estados Unidos la vacunación ha avanzado rápido y los ciudadanos de estas naciones de habla inglesa ya se están reactivando económicamente pues no se tienen tantas restricciones. 

### Top twiteros
![alt text](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/4_Covid19/Visualizaciones/TopTuiteros.png)

**Análisis:** En esta gráfica se buscaba encontrar indicios sobre fuentes oficiales que estén abordando el tema del covid 19. Sin embargo, se han encontrado cuentas de usuarios que tuitean con normalidad sin llegar al punto de ser bots automatizados. 

### Lugares donde se tuitea sobre el covid 19
![alt text](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/4_Covid19/Visualizaciones/Principales_lugares_donde_twitean.png)

**Análisis:** La gráfica nos indica de que lugares del mundo están tuiteando temas en torno al covid 19 a nivel mundial, en nuestro caso están lugares como Philadelphia, Nigeria, Venezuela, New York.
**En conclusion:** los datos recopilados nos permiten tener una vista general de cómo está el tema del covid a nivel mundial, si bien se está hablando mayoritariamente en el habla inglesa. Los datos referentes a locación nos hacen tomar en cuenta que países latinoamericanos como Venezuela están hablando del tema pues ciertos países no tienen planes de vacunación inmediatos para su población. 

