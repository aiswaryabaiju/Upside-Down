#!/usr/bin/python

"""
This code executes a search request for the specified search mood.
It takes in a Youtube API key provided by the developer
It randomizes the top results and returns a random URL based on what mood was
called
"""

import argparse
import logging
import json
import random

from pprint import pprint
#Importing all the required libraries 

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
#Makes the youtube request annd parses it


DEVELOPER_KEY = 'AIzaSyCEGv-JQcjMIdpXYO9eIhAGWKLJn1XzXos'       #Key
YOUTUBE_API_SERVICE_NAME = 'youtube'                            #API keys
YOUTUBE_API_VERSION = 'v3'                                      #API version

def mood_eval_youtube(keyword, limit):
    """
    This function finds the videos which correlate with the specified mood 
    and returns the list of the URLs of the videos.

    Args:
        keyword(str): The mood
        limit (int): The number to be returned.

    Returns:
        A list of URL code.
    """
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey = DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    # Calls the search response to search for the   list from Youtube
    search_response = youtube.search().list(q=keyword, part='id,snippet',
                                            maxResults=limit)
    search_response = search_response.execute()

    # Create an empty list of videos  
    videos = []


    # Add each result to the appropriate list, and then display the lists of
    # matching videos.
    for search_result in search_response.get('items', []):  
        if search_result['id']['kind'] == 'youtube#video':   
            video_id = search_result['id']['videoId']
            video_url = "https://www.youtube.com/watch?v={0}".format(video_id)
            videos.append(video_url)

    return videos

if __name__ == '__main__':
    try:
        print(mood_eval_youtube("happy", 50))
    except HttpError as e:
        print ('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
