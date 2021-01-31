from __future__ import absolute_import, print_function

import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from time import time


consumer_key = "TEecqFGOVxIAmkCNqFsXYuyHN"
consumer_secret = "I1jf3nNCVOk5jrv64lzuAa0mgwc2FvncngNdtmI8dn1CE4QbNa"

access_token = "1333839067344203780-pc5mGS3URQ5nfFTwchRQnZhEBNYVtY"
access_token_secret = "7IC605Jpx2reYeEEmEezC33iLVCBZNBtHmIiIJzuqjPWA"


class StdOutListener(StreamListener):
    """A listener handles tweets that are received from the stream. """
    def __init__(selfself, time_limit=60):
        selfself.start_time = time()
        selfself.limit = time_limit
        selfself.saveFile = open('output.json', 'a')
        super(StdOutListener, selfself).__init__()

    def on_data(self, data):

        if(time() - self.start_time < self.limit):

            # convert data to a json object to retrieve only created_at fields
            j = json.loads(data)

            if 'created_at' in j:
                # if j['country_code'] is "US":
                    # write to the file
                    self.saveFile.write(data)
            return True
        else:
            self.saveFile.close()
            return False

    def on_error(self, status_code):
        print(status_code)


if __name__ == '__main__':

    l = StdOutListener(time_limit=60)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)

    # tweets sent from amsterdam (uncomment this or the filter method on line 56)
    # stream.filter(locations=[4.61, 52.27, 5.07, 52.50])

    # tweets related to covid-19
    # stream.filter(track= ["working from home", "stay at home", "stay-at-home", "work-from-home", "work from home", "stayathome" ])
    stream.filter(track= ["Covid19", "coronavirus", "corona virus", "covid-19" ])
