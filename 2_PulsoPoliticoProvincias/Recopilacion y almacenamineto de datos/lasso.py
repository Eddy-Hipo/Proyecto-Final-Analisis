import tweepy
import json
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#Conexion a couchddb
ckey = "N31wuT1bPEiM2cmx8ccu1orxb"
csecret = "O4avAsvM6g10JCgRzAnq3mv2QvBqve518tB4ix78dT6u3DAtvh"
atoken = "360193692-rekUZMqpMZFsnVvXovgqCuuVfwtp3aO4gui2O8zl"
asecret = "BW1PeKHghRdZ8YUxYbizidV043U3P7ysxXJvZk8i6AWJX"
class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        if "Lasso" in dictTweet["text"].lower() : 
            try:
                dictTweet["_id"] = str(dictTweet['id'])
                doc = db.save(dictTweet)
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
server = couchdb.Server('http://admin:brenda@localhost:5984/')  
try:
    db = server.create('twitter-proyecto-lasso')
except:
    db = server['twitter-proyecto-lasso']
twitterStream.filter(locations=[-92.21,-5.02,-75.19,1.88])