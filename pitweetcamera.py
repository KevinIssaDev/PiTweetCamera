from gpiozero import Button, LED, TrafficLights, MotionSensor
from picamera import PiCamera
from datetime import datetime
from signal import pause
from json import load
import tweepy


def vrint(content):
    """ Verbose printing for debugging """
    if verbose:
        print(content)


def timestamp_format(timestamp, filename=False, ext="jpg"):
    """ Formats timestamp to string """
    if filename:
        # 'day-month-year@hour;minute.jpg'
        return timestamp.strftime('%d-%m-%Y@%H;%M;%S.' + ext)
    else:
        # Day Month Date Hour:Minute:Second year
        return timestamp.strftime('%c')


def load_auth_tokens(auth_file):
    """ Loads the authentication tokens from 'auth_file' """
    with open(auth_file, 'r') as f:
        auth_tokens = load(f)
    vrint("Authentication tokens loaded.")
    return auth_tokens


def tweet(content, media=False, media_path=None):
    """ Tweets the content with or without media """
    if media:
        api.update_with_media(media_path, content)
    else:
        api.update_status(content)


def on_motion():
    """ Takes a photo then records until movement stops """
    lights.red.off()
    lights.amber.blink()
    vrint("Motion detected!")
    thumbnail_capture_time = datetime.now()
    thumbnail_filename = timestamp_format(thumbnail_capture_time, filename=True)
    camera.capture(thumbnail_filename)
    vrint("Thumbnail captured.")
    vrint("Recording...")
    camera.start_recording(timestamp_format(datetime.now(), filename=True, ext='h264'))
    tweet("Motion detected at {}!".format(timestamp_format(thumbnail_capture_time)), media=True, media_path=thumbnail_filename)
    vrint("Posted to Twitter.")


def on_no_motion():
    """ Stops the recording when there's no movement """
    lights.amber.off()
    lights.red.on()
    camera.stop_recording()
    vrint("Recording done.")


def on_button_press():
    """ Takes a photo when the button is pressed """
    lights.red.off()
    lights.green.on()
    vrint("Photo captured.")
    camera.capture(timestamp_format(datetime.now(), filename=True))
    lights.green.off()
    lights.red.on()


if __name__ == "__main__":
    button = Button(17)
    sensor = MotionSensor(15)
    lights = TrafficLights(2, 3, 4)
    lights.red.off()
    lights.amber.off()
    lights.green.off()
    camera = PiCamera()
    verbose = True
    auth_tokens = load_auth_tokens('twitter_auth.json')
    auth = tweepy.OAuthHandler(auth_tokens['consumer_key'], auth_tokens['consumer_secret'])
    auth.set_access_token(auth_tokens['access_token'], auth_tokens['access_token_secret'])
    api = tweepy.API(auth)
    lights.red.on()
    sensor.when_motion = on_motion
    sensor.when_no_motion = on_no_motion
    button.when_pressed = on_button_press
    pause()
