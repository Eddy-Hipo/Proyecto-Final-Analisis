# Videojuegos en Línea del mundo.
## 1. Arquitectura
![alt text](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/3_Juegos/DataLake_Juegos.png)
## 2. Scripts de extracción, filtrado y exportación de datos
### Kaggle
#### _(Games.csv)_ [Archivo de Kaggle](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/3_Juegos/Recopilacion%20y%20almacenamiento%20de%20datos/Games.csv)
Los datos estáticos se obtuvieron de la página Kaggle (https://www.kaggle.com/sidtwr/videogames-sales-dataset) <br/>
Los datos descargados en formato CSV no se necesitaron filtrar para  realizar las visualziaciones. Es decir se utilizarán **directamente** en la aplicación RapidMiner.
### Tik-Tok Scraping
#### _(videogamesceo.csv)_ [Archivo de Tik-Tok sin filtrar](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/3_Juegos/Recopilacion%20y%20almacenamiento%20de%20datos/videogamesceo/videogamesceo.csv)
Se recopilaron los datos de las publicaciones de videojuegos del usuario "videogamesceo" (https://www.tiktok.com/@videogamesceo?lang=es) <br/>
Con el objetivo de adquirir registros de datos relacionados con el tema.
Para realizar esta tarea se ejecutó el comando: tiktok-scraper user videogamesceo -n 300 -t csv , directamente en la línea de comandos del sistema operativo.
### - Script 1 - Filtrado de datos de Tik-Tok Scraping
#### _(filtrado-datos-tiktok.py)_ [Script del Filtrado](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/3_Juegos/Recopilacion%20y%20almacenamiento%20de%20datos/videogamesceo/filtrado-datos-tiktok.py)
Con el objetivo de adquirir registros de datos relacionados con el tema, se implemeto un filtrado donde se extrajeron unicamente las columnas más relevantes como: 
* Texto 
* Nombre del autor
* Fecha de creación
* Nombre de la música
* Número de compartidos
* Número de comentarios
* Número de reproducciones
* Hashtags
Una vez filtrada la información se guardaron en un archivo tipo CSV llamado [Tik-Tok-filtrado](https://github.com/Eddy-Hipo/Proyecto-Final-Analisis/blob/main/3_Juegos/Recopilacion%20y%20almacenamiento%20de%20datos/videogamesceo/Tik-Tok-filtrado.csv)
## 3. Visualizaciones y análisis con la herramienta RapidMiner
### Juegos Lanzados por Compañia Desarrolladora
<img src="Visualizaciones/Juegos%20Lanzados%20por%20compañía.png" width="1000"/><br/>
**Análisis:** La gráfica muestra la cantidad de juegos más jugados desarrollados por cada compañia, teniendo como mejores empresas a Electronic Arts y Sony Computer Entertainment.
### Juegos más Populares en el Mundo
<img src="Visualizaciones/Juegos%20más%20popularesen%20el%20mundo.png" width="1000"/><br/>
**Análisis:** La gráfica muestra al juego preferido por los jugadores alrededor del mundo, dando como resultado que el mejor juego en línea en este momento es Grand Theft Auto V
### Juegos por Género
<img src="Visualizaciones/Juegos%20por%20Géneros.png" width="1000"/><br/>
**Análisis:** La gráfica muestra el género de juego preferido por los usuarios, dando como resultado que los juegos de Acción y Shooter son los juegos que tiene más acogida por los Gamers del mundo.
### Jugadores por Paises
<img src="Visualizaciones/Jugadores%20por%20países.png" width="1000"/><br/>
**Análisis:** La gráfica muestra el númeo de jugadores de un juego en específico por continente, dando como resultado que en Europa se encuentra la mayor cantidad de jugadores para Grand Theft Auto V y FIFA 18.
