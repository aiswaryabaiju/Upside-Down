"""
Module defines the utilities for fetching the music from the Spotify API.
"""

import json
import random

import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

class spotify_api:
    """
    Class that uses that spotify api to get a random song depending on the mood
    of the user.
    """

    def __init__(self, emotion):
        """
        Constructor initialiazes spotify instance and client ID and key.
        
        Args:
            emotion (str): String represents the emotion.
        """

        self.__clientID = '0ba2ff8c64394b11b98626001a7d9439'
        self.__key= 'ee1a06ad1f2c44c7bb5fccb6adbb3672'
        self.__redirectURI = 'http://localhost:8888/callback'
        client_credentials_manager = \
            SpotifyClientCredentials(client_id=self.__clientID,
                                     client_secret=self.__key)
        self.__sp = \
            spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        self.__emotion = emotion

    def search_emotion(self):
        """
        Gets a list of playlists based on the emotion that is given.

        Returns:
            list of the json objects of top 50 the playlists that were found.
        """

        result = self.__sp.search(q=self.__emotion, limit= 50, type='playlist')
        return result['playlists']['items']

    def get_random_playlist(self):
        """
        Get a random playlist from the list
        
        Returns:
            the name of the playlist as a string
        """

        playlist_list = self.search_emotion()
        index = random.randrange(0,len(playlist_list))
        return (playlist_list[index]['name'])
    
    def search_playlist(self):
        """
        searches for top 50 songs based on the playlist

        Returns:
            a list of json objects that contain the names of the songs from
            the given playlist

        """
        playlist = self.get_random_playlist()
        result = self.__sp.search(q=playlist,limit=50, type='track')
        return result['tracks']['items']
    
    def get_random_song(self):
        """
        Gets the song and and link from a given object and its Link

        Returns:
            a list of strings that contains the song name and the link
        """

        song_list = self.search_playlist()
        song_data = []
        for i in range(0, len(song_list)):
            song_data.append(song_list[i]['external_urls']['spotify'])
        return song_data
        

#test delete later
x = spotify_api('happy')
print(x.get_random_song())
