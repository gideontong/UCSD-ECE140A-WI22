from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse

import sqlite3


def get_home(req):
    return FileResponse("index.html")


def value(req):
    # get the id from the request
    age = req.matchdict['age']
    height = req.matchdict['height']

    # connect to the database
    db = sqlite3.connect('data.db')
    cursor = db.cursor()

    height_low = {
        '1': 150,
        '2': 160,
        '3': 170,
        '4': 180
    }

    height_high = {
        '1': 160,
        '2': 170,
        '3': 180,
        '4': 190
    }

    age_low = {
        '1': 20,
        '2': 30,
        '3': 40,
        '4': 50,
        '5': 60
    }

    age_high = {
        '1': 30,
        '2': 40,
        '3': 50,
        '4': 60,
        '5': 70
    }

    # query the database with the id
    cursor.execute(
        "SELECT id, name, owner, height, age FROM Gallery WHERE age >= ? AND age < ? AND height >= ? AND height < ?;", (age_low[age], age_high[age], height_low[height], height_high[height]))
    record = cursor.fetchone()
    db.close()

    # if no record found, return error json
    if record is None:
        return {
            'error': "No data was found for the given ID",
            'img': "",
            'name': "",
            'designation': "",
            'email': ""
        }

    # populate json with values
    response = {
        'id':           record[0],
        'name':         record[1],
        'owner':  record[2],
        'height':        record[3],
        'age': record[4]
    }

    return response


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_view(get_home, route_name='home')
        config.add_route('value', '/value/{age}/{height}')
        config.add_view(value, route_name='value', renderer='json')
        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    print('Web server started on: http://0.0.0.0:6543')
    server.serve_forever()
