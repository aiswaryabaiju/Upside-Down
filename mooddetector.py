import requests
import logging

API_URL = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false"
API_KEY_1 = "8cd2115e508b4f0c8997a6283e90f5f0"
API_KEY_2 = "4cd7b83eae764e6cbf820b7193192e2c"
API_FORMAT = "application/json"

def make_api_call(image):
    """
    Makes the API call to the Microsoft Cognitive API with the specified image
    and returns the raw JSON data from it.

    Args:
        image (str): The URL of the image to be sent to the API.

    Returns:
        The JSON data returned by the API call. If the request fails, None is
        returned instead.
    """

    # Set up the headers for the API
    headers = dict()
    headers["Ocp-Apim-Subscription-Key"] = API_KEY_1
    headers["Content-Type"] = API_FORMAT

    # Set the JSON field to store the URL of the image
    json = {
        "url": image
    }

    # Make an HTTP request for the API
    response = requests.request("post", API_URL, headers=headers, json=json)

    # Print HTTP response code and data
    print(response.status_code)
    print(response.content)

if __name__ == "__main__":
    # Test API on simple image with a humanoid
    TEST_IMAGE = "https://scontent-ort2-1.xx.fbcdn.net/v/t34.0-12/28313695_1635841079808552_878984412_n.jpg?oh=2124924de94bf3aa43308efde86de1a4&oe=5A939EB6"
    make_api_call(TEST_IMAGE)