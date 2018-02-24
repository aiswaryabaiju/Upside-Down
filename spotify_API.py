import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import random

class spotify_api:

    def __init__(self):
        self.__clientID = '0ba2ff8c64394b11b98626001a7d9439'
        self.__key= 'ee1a06ad1f2c44c7bb5fccb6adbb3672'
        self.__redirectURI = 'http://localhost:8888/callback'
        client_credentials_manager = SpotifyClientCredentials(client_id=self.__clientID, client_secret=self.__key)
        self.__sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def search_emotion(self, emotion):
        result = self.__sp.search(q=emotion, limit= 50, type='playlist')
        return result['playlists']['items']

    def get_random_playlist(self,e):
        playlist_list = self.search_emotion(emotion=e)
        index = random.randrange(0,50)
        return (playlist_list[index]['name'])
    
    def search_playlist(self,e):
        playlist = self.get_random_playlist(e=e)
        result = self.__sp.search(q=playlist,limit=50, type='track')
        return result['tracks']['items']
    
    def get_random_song(self,e):
        song_list =  self.search_playlist(e=e)
        index = random.randrange(0,50)
        song_data = []
        song_data.append(song_list[index]['name'])
        song_data.append(song_list[index]['external_urls']['spotify'])
        return song_data
        

#test
x = spotify_api()
print(x.get_random_song('happy'))