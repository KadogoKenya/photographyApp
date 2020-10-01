from flask import render_template
from app import app

# from .request import search_image


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@app.route('/search')
def search_images(image_name):
    '''
    View function to display the search results
    '''
    image_name_list = image_name.split(" ")
    image_name_format = "+".join(image_name_list)
    searched_images = search_image(image_name_format)
    title = f'search results for {image_name}'
   
    return render_template('search.html',images = searched_images)