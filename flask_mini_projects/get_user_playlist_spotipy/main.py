'''
setup flask web server
interact with the spotify API
using spotipy library
'''
import os
from flask import Flask,session,redirect,url_for,request
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
    redirect_uri=redirect_uri,
    scope=scope,
    cache_handler=cache_handler,
    show_dialog=True
)
sp=Spotify(auth_manager=sp_oauth)

@app.route('/')
def home():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url=sp_oauth.get_authorize_url()
        return redirect(auth_url)
    return redirect(url_for('get_playlist'))

@app.route('/callback')
def callback():
    sp_oauth.get_access_token(request.args['code'])
    return redirect(url_for('get_playlist'))

@app.route('/get_playlist')
def get_playlist():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url=sp_oauth.get_authorize_url()
        return redirect(auth_url)
    
    playlist=sp.current_user_playlists()
    playlist_info=[(plist['name'],plist['external_urls']['spotify']) for plist in playlist['items']]
    playlist_html='<br>'.join([f'{name}:{url}' for name,url in playlist_info])

    return playlist_html

@app.route('/logout')
def logout():
    session.clear()
    redirect(url_for('home'))

@app.route('/greetings')
def greetings():
    return 'Hello {}. Thank you for visiting Spotify music'.format('music-lover254')

if __name__=='__main__':
    app.run(debug=True)