from app import app
import urllib.request,json
from .models import Image



api_key = app.config['API_KEY']
base_url = app.config["API_BASE_URL"]

    
# image_results=[]


def search_images(photo_type):
    search_image_url = 'https://pixabay.com/api/?key={}&q={}&image_type=photo').format(api_key,photo_type)
    

    with urllib.request.urlopen(search_image_url) as url:
        search_image_data = url.read()
        search_image_response = json.loads(search_movie_data)

        search_image_results = None

        if search_image_response['results']:
            image_list = search_image_response['results']
            image_results = process_results(image_list)

    return image_results