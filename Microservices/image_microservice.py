import requests
import json


website_url = 'https://pixabay.com/api/'

# key_file = open('./text_files/key.txt', 'r')
# api_key = key_file.read()
# key_file.close()

# API Key is hardcoded for now, will be changed to a user-specific key
api_key = '27355476-1d1fe048b2ee489de0bd48717'


def get_image_url(city, large=False):
    """
    takes a string city, returns url of image
    large parameter toggles large or standard size image
    """
    request_url = website_url + '?key=' + api_key + '&q=' + city
    img_request = requests.get(request_url)
    img_data = json.loads(img_request.text)
    try:
        top_result = img_data['hits'][0][('webformatURL', 'largeImageURL') [large]]
    except:
        raise Error()

    return top_result