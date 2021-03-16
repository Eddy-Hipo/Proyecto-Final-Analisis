import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
###API ########################
ckey = "nhB43XVAOFeM82rlxdKf6Tw7J"
csecret = "h4nHSJtjUaQY49uzup3YbHtepgA0SfE1iw4dJMWxlshqUZVoVP"
atoken = "1100216660814909440-jlkErRdRHDf8012Ww1TQSmyU0ABOEI"
asecret = "DMne0eaoXGxY45Jn6ZF4suJF6LjYrG5SVojZ9XXrLuxST"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
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
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:sistemas@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('examen2-covid')
except:
    db = server['examen2-covid']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[-78.619545,-0.408764,-78.259892,-0.047208])  
twitterStream.filter(track=['Covid_19', 'covid', 'CoronavirusEnEcuador', 'coronavirus'])