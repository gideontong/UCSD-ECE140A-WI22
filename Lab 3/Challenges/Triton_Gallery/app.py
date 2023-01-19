# import all the necessary libraries
from statistics import median
from wsgiref.simple_server import make_server
from cv2 import mean
from numpy import std
from pyramid.config import Configurator
from pyramid.response import FileResponse

from random import randint
import cv2

def index_page(req):
    return FileResponse("index.html")



def get_price(id):
    img = cv2.imread(f'public/{id}.jpg')
    img = cv2.Canny(img, 60, 200)
    return mean(img + median(img) * std(img)) + img.shape[2]


# Main entrypoint
if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_view(index_page, route_name='home')

        config.add_route('price', '/price/{id}')
        config.add_view(get_price, route_name='price')

        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app) # Start the application on port 6543
    server.serve_forever()


