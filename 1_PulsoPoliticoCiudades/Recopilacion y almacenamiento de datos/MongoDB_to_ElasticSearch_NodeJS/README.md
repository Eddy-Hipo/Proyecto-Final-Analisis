# Tomar los datos de MongoDB a ElasticSearc.
Al utilizar node.js puede utilizar algun IDE para Javascript, en este caso se uso WebStorm.

## 1. Instalación
Instalar las dependencias del proyecto con: 

npm install 

## 2. Configuración de MongoDb y ElasticSearch
### - Editar el archivo en config/
#### _(default.json)_
Cambiar la configuración de ElasticSearch o MongoDb dependiendo de su caso. En este royecto se manejo de manera local por lo que esta la url como localhost.
En la sección de "elasticsearch": 
La pate de "elasticsearchIndices" al ubicar el objeto "TwitterProyectoArauz" hace referencia al nombre de la base guardada en MongoDB pero este puede editarse, los valores de index y type son a eleccion. en la parte de collectionName poner el nombre de la colección de MongoDb que se desea enviar a elastic.
En la seccion de "mongodb" : 


## 
### - Editar el archivo en app.js
#### _(app.js)_
Si en el archivo default.json se ha cambiado el nombre del objeto en elasticsearchIndices que hace referencia a la creación del index en elasticsearch, modificar lo siguiente: 
En la variables de indexname, indextype y tableName, verificar que se este llamando correctamente a la configuración del archivo config/default.json. 

## 2. Utilizar el proyecto
### - Correr el script
#### _(En la terminal de su IDE o si tiene la gitBash)_
Ejecutar el comando:
node app.js

## 4. Explicación
### - Al correr el script ocurre lo siguiente:
Una vez ejecute el comando en la terminal, se hara uso de la funcion IndexMongodbData la cual se encuentra en el archivo "indexer.js" la cual primero va verificar la conexión al servidor  de MongoDb, y con los parametros enviados procede a leer la colección e identificar el elemento de "created_at"  para formatear la fecha. Posterior a esto modifica la sección de index que maneja elastic y finalmente lo agrega en un vector para subirlo a ElasticSearch.  
### - Imagen de referencia
![alt text](https://raw.githubusercontent.com/Eddy-Hipo/Proyecto-Final-Analisis/main/1_PulsoPoliticoCiudades/Recopilacion%20y%20almacenamiento%20de%20datos/MongoDB_to_ElasticSearch_NodeJS/CapturaDeReferencia.png)





