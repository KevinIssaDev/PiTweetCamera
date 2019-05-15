from gpiozero import Button, LED
from picamera import PiCamera
from time import sleep
from datetime import datetime
from signal import pause
from json import load
import tweepy
#sudo pip3 install tweepy

def vrint(content):
    """ Verbose printing for debugging """
    if verbose == True:
        print(content)

def timestamp_filename(timestamp):
    """ Formats a filename from timestamp

    'day-month-year@hour;minute.png'
    """
    return timestamp.strftime('%d-%m-%Y@%H;%M.png')

def load_auth_tokens(auth_file):
    """ Loads the authentication tokens from 'auth_file' """
    with open(auth_file, 'r') as f:
        auth_tokens = load(f)
    vrint("Authentication tokens loaded.")
    return auth_tokens

def tweet(api, media = False, media_path = None, content):
    """ Tweets the content with or without media """
    if media:
        api.update_with_media(media_path, content)
    else:
        api.update_status(content)

# def capture_photo():
#     pass


if __name__ == "__main__":
    #button = Button(14)
    #camera = PiCamera(14)
    verbose = True
    auth_tokens = load_auth_tokens('twitter_auth.json')
    auth = tweepy.OAuthHandler(auth_tokens['consumer_key'], auth_tokens['consumer_secret'])
    auth.set_access_token(auth_tokens['access_token'], auth_tokens['access_token_secret'])
    api = tweepy.API(auth)
    #timestamp_filename(datetime.now())
