from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse

import sqlite3


def get_home(req):
    return FileResponse("index.html")


def value(req):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Data;')
    record = cursor.fetchone()
    db.close()

    # if no record found, return error json
    if record is None:
        return {
            'error': 'No data found.'
        }

    response = {
        'distance': record[0],
        'x': record[1],
        'y': record[2],
        'z': record[3]
    }

    return response


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_view(get_home, route_name='home')
        config.add_route('value', '/value')
        config.add_view(value, route_name='value', renderer='json')
        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    print('Web server started on: http://0.0.0.0:6543')
    server.serve_forever()
