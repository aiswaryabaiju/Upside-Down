import requests
import logging

API_URL = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false"
API_KEY_1 = "8cd2115e508b4f0c8997a6283e90f5f0"
API_KEY_2 = "4cd7b83eae764e6cbf820b7193192e2c"
API_FORMAT = "application/octet-stream"

def make_api_call(image):
    """
    Makes the API call to the Microsoft Cognitive API with the specified image
    and returns the raw JSON data from it.

    Args:
        image (bytearray): The bytearray representation of the image data.

    Returns:
        The JSON data returned by the API call. If the request fails, None is
        returned instead.
    """

    # Set up the headers for the API
    headers = dict()
    headers["Ocp-Apim-Subscription-Key"] = API_KEY_1
    headers["Content-Type"] = API_FORMAT

    # Make an HTTP request for the API
    response = requests.request("post", API_URL, headers=headers, data=image)

    # Print HTTP response code and data
    print(response.status_code)
    print(response.content)

if __name__ == "__main__":
    # Test API on simple image with a humanoid
    TEST_IMAGE_PATH = "res/deepu_bee.jpg"
    test_image_data = None
    with open(TEST_IMAGE_PATH, "rb") as f:
        test_image_data = f.read()
    
    make_api_call(test_image_data)
