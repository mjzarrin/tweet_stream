from tweepy import OAuthHandler, Stream, StreamListener
import json


mytrack = ['netmine', 'bitkhar', 'tesla', 'bitcoin']

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class StdOutListener(StreamListener):
    def __init__(self, listener, track_list, repeat_times):
        self.repeat_times = repeat_times
        self.track_list = track_list
        print('************** initialized : #', self.repeat_times)

    def on_data(self, data):
        print(self.repeat_times, 'tweet id : ', json.loads(data)['id'])

    def on_exception(self, exception):
        print('exception', exception)
        new_stream(auth, self.track_list, self.repeat_times+1)

    def on_error(self, status):
        print('err', status)
        if status == 420:
            # returning False in on_data disconnects the stream
            return False


def new_stream(auth, track_list, repeat_times):
    listener = StdOutListener(StreamListener, track_list, repeat_times)
    stream = Stream(auth, listener).filter(track=track_list, is_async=True)


new_stream(auth, mytrack, repeat_times=0)
