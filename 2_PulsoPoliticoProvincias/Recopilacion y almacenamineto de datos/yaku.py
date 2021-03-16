import tweepy
import json
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#Conexion a couchddb
ckey = ""
csecret = ""
atoken = ""
asecret = ""
class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        if "pachakutik" in dictTweet["text"].lower() : 
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
    db = server.create('twitter-proyecto-yaku')
except:
    db = server['twitter-proyecto-yaku']
twitterStream.filter(locations=[-92.21,-5.02,-75.19,1.88])