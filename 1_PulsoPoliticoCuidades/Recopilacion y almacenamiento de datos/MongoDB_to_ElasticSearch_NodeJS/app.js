var indexer = require('./indexer.js');

var config = require ('config');

var indexname = config.elasticsearch.elasticsearchIndices.TwitterProyectoArauz.index;
var indextype = config.elasticsearch.elasticsearchIndices.TwitterProyectoArauz.type;
var tableName = config.elasticsearch.elasticsearchIndices.TwitterProyectoArauz.collectionName;

indexer.IndexMongodbData(indexname,indextype,tableName); //Inserting bulk data into Elasticsearch, Kibana from mongodb


