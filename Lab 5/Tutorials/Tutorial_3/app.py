from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse

import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv()

''' Environment Variables '''
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

def get_home(req):
    return FileResponse("index.html")


def get_staff_member(req):
    # get the id from the request
    id = req.matchdict['staff_id']

    # connect to the database
    db = mysql.connect(host=db_host, user=db_user,
                       passwd=db_pass, database=db_name)
    cursor = db.cursor()

    # query the database with the id
    cursor.execute(
        "SELECT id,name,designation,email FROM TeachingStaff WHERE id='%s';" % id)
    record = cursor.fetchone()
    db.close()

    # if no record found, return error json
    if record is None:
        return {
            'error': "No data was found for the given ID",
            'id': "",
            'name': "",
            'designation': "",
            'email': ""
        }

    # populate json with values
    response = {
        'id':           record[0],
        'name':         record[1],
        'designation':  record[2],
        'email':        record[3]
    }

    return response


if __name__ == '__main__':
    with Configurator() as config:
        app = config.make_wsgi_app()
        config.add_route('get_staff_member', '/staff/{staff_id}')
        config.add_view(get_staff_member, route_name='get_staff_member', renderer='json')
        config.add_route('home', '/')
        config.add_view(get_home, route_name='home')

    server = make_server('0.0.0.0', 6543, app)
    print('Web server started on: http://0.0.0.0:6543')
    server.serve_forever()
