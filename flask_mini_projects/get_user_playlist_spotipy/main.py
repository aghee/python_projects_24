'''
setup flask web server
interact with the spotify API
using spotipy library
'''
import os
from flask import Flask,session
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler



app=Flask(__name__)
app.config['SECRET_KEY']=os.urandom(64)

client_id='3ff52204556b4397a906e23981c89db8'
client_secret='37f3dc432cd645e694cc117fa2790436'
redirect_uri='http://localhost:5000/callback'
scope='playlist-read-private'

cache_handler=FlaskSessionCacheHandler(session)
sp_oauth=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri='http://localhost:5000/callback'
    scope='playlist-read-private'
)

if __name__=='__main__':
    app.run(debug=True)