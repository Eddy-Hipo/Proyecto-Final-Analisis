#pip install pymongo
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from pymongo import MongoClient

#Conexion a mongodb
server= MongoClient()#Inicializarobjeto
server= MongoClient("mongodb://localhost:27017")#Indicarparametrosdel servidor
bd= server.TwitterProyectoArauz#SeleccionarSchema
db = bd.Ciudades#SeleccionarColeccion

ckey = ""
csecret = ""
atoken = ""
asecret = ""

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        if "arauz" in dictTweet["text"].lower() : 
            try:
                dictTweet["_id"] = str(dictTweet['id'])
                doc = db.insert_one(dictTweet)
                print ("SAVED" + str(doc) +"=>" + str(data))
            except:
                print ("Already exists")
                pass
            return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
streamListen=listener()
twitterStream = Stream(auth, streamListen)

#Filtro para todo el Ecuador
twitterStream.filter( locations=[-92.21,-5.02,-75.19,1.88])
