"""
This module describes the Mood Evaluator which returns links to GIFs depending
on the user mood.
"""

import ast
import logging
import random
import time

import giphy_client

from giphy_client.rest import ApiException
from pprint import pprint

# API instance and key
API_INSTANCE = giphy_client.DefaultApi()
API_KEY = "MOOU8sSR5RnuORvyRNC2WUZAwYbD50Fo"

# Parameters for the API requests
API_FORMAT = 'json'
API_OFFSET = 0
API_RATING = 'g'
API_LANG = 'en'

def mood_eval_gif(keyword, limit):
    """
    This function finds GIFs which correlate with the specified mood and
    returns a list of the URL to the GIFs.

    Args:
        keyword (str): The mood.
        limit (int): Maximum number of of GIFs to be returned.

    Returns:
        A list of URLs to the GIFs.
    """

    # Stores a list of URLs to be returned
    urls = []

    try:
        # Fetch the API response and convert it to a JSON map
        api_response = API_INSTANCE.gifs_search_get(API_KEY, keyword,
                                                    limit=limit,
                                                    offset=API_OFFSET,
                                                    rating=API_RATING,
                                                    lang=API_LANG,
                                                    fmt=API_FORMAT)
        api_response = str(api_response)
        api_response = ast.literal_eval(api_response)

        # For each GIF in the API response, get the URL and store into list
        for image in api_response["data"]:
        	image_url = (image["images"]["original"]["url"])
        	urls.append(image_url)

        # Return the URLS
        return urls
    except ApiException as e:
        logging.error("Failed to fetch GIF data: '%s'", str(e))
        raise

# Print the 50 GIFs for keyword 'happy'
if __name__ == "__main__":
    print(mood_eval_gif("happy", 50))
