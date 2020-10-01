from flask import render_template,request,redirect,url_for
from app import app
from .requests import search_images

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   
    title = 'Home - Welcome to The best image view Website Online'

    search_image = request.args.get('search_query')

    if search_image:
        return redirect(url_for('search',name=search_image))
    else:
        return render_template('index.html')





@app.route('/search')
def search(name):
    '''
    View function to display the search results
    '''
    image_name_list = image_name.split(" ")
    image_name_format = "+".join(image_name_list)
    searched_images = search_image(image_name_format)
    title = f'search results for {name}'
   
    return render_template('search.html',images = searched_images)