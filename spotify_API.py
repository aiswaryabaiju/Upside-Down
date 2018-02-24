import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
class spotify_api:

    def __init__(self):
        self.__clientID = '0ba2ff8c64394b11b98626001a7d9439'
        self.__key= 'ee1a06ad1f2c44c7bb5fccb6adbb3672'
        self.__redirectURI = 'http://localhost:8888/callback'
        client_credentials_manager = SpotifyClientCredentials(client_id=self.__clientID, client_secret=self.__key)
        self.__sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def search_emotion(self, emotion):
        result = self.__sp.search(q=emotion, limit= 50, type='playlist')
        


x = spotify_api()
x.search_emotion()