from pyramid.config import Configurator
from pyramid.response import Response, FileResponse
from time import sleep
from wsgiref.simple_server import make_server
from RpiMotorLib import RpiMotorLib

import cv2
import numpy as np
import os
import serial
import sqlite3
import sys
import webbrowser

try:
    import RPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO

gpgga_info = "$GPGGA,"
ser = serial.Serial("/dev/serial0")
GPGGA_buffer = 0
NMEA_buff = 0
lat_in_degrees = 0
long_in_degrees = 0

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

GpioPins = [18, 23, 24, 25]
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")


def motor_turn(callback, *args):
    for i in range(50):
        mymotortest.motor_run(GpioPins, .002, 5, False, False, "full", .05)
        callback(*args)
    for i in range(50):
        mymotortest.motor_run(GpioPins, .002, 5, True, False, "full", .05)
        callback(*args)
    GPIO.cleanup()


def find_item(lower1, upper1):
    frames = 0

    if not os.path.exists("./Frames/"):
    os.mkdir("./Frames/")
    print("Created new directory for logging frames")

    while(frames >= 0):
        _, frame = cap.read()
        frames += 1
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower2 = np.array([160, 100, 20])
        upper2 = np.array([179, 255, 255])

        red_only1 = cv2.inRange(hsv, lower1, upper1)
        red_only2 = cv2.inRange(hsv, lower2, upper2)
        red_only = red_only1 + red_only2
        mask = np.ones((5, 5), np.uint8)
        opening = cv2.morphologyEx(red_only, cv2.MORPH_OPEN, mask)
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
            opening, 4, cv2.CV_32S)

        b = np.matrix(labels)

        if num_labels > 1:
            max_label, max_size = max([(i, stats[i, cv2.CC_STAT_AREA])
                                       for i in range(1, num_labels)], key=lambda x: x[1])
            seg = (b == max_label)
            seg = np.uint8(seg)
            seg[seg > 0] = 255

            cv2.imwrite(f"./Frames/data_{frames}.png", frame)
            cv2.imwrite(f"./Frames/seg_{frames}.png", seg)

        return max_label, max_size


def convert_to_degrees(raw_value):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" % (position)
    return position


def GPS_Info():
    global NMEA_buff
    global lat_in_degrees
    global long_in_degrees
    nmea_time = []
    nmea_latitude = []
    nmea_longitude = []
    nmea_time = NMEA_buff[0]
    nmea_latitude = NMEA_buff[1]
    nmea_latitude_dir = NMEA_buff[2]
    nmea_longitude = NMEA_buff[3]
    nmea_longitude_dir = NMEA_buff[2]

    lat = float(nmea_latitude)
    longi = float(nmea_longitude)

    lat_in_degrees = convert_to_degrees(
        lat) if nmea_latitude_dir == 'N' else (-1 * convert_to_degrees(lat))
    long_in_degrees = convert_to_degrees(
        longi) if nmea_latitude_dir == 'N' else (-1 * convert_to_degrees(lat))

    return lat_in_degrees, long_in_degrees


def get_home(req):
    return FileResponse("index.html")


def value(s):
    global record, sk
    sk = s
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute(f'SELECT {s} FROM objects;')
    record = cursor.fetchone()
    db.close()

    if record is None:
        return {
            'error': 'ERROR: Could not be found.'
        }

    response = {
        'hl': f'LOW HUE: {record[1]}',
        'sl': f'LOW SATURATION: {record[2]}',
        'vl': f'LOW VALUE: {record[3]}',
        'hh': f'HIGH HUE: {record[4]}',
        'sh': f'HIGH SATURATION: {record[5]}',
        'vh': f'HIGH VALUE: {record[6]}'
    }

    return response


def gps(req):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute(f'SELECT {sk} from found_objects;')
    record = cursor.fetchone()
    v = 0
    while record is not None:
        v += 1
        r = f'{sk}{v}'
        cursor.execute(f'SELECT {r} from found_objects;')
    
    cursor.execute('INSERT INTO found_objects VALUES (?, ?, ?)', (None, r, str((lat_in_degrees, long_in_degrees))))

    db.close()
    return {
        'lat': lat_in_degrees,
        'lon': long_in_degrees
    }


def apple(req):
    return value('apple')


def orange(req):
    return value('orange')


def banana(req):
    return value('banana')


def run(req):
    label, size = find_item(record[1:4], record[4:7])
    while size < 1:
        motor_turn(find_item, record[1:4], record[4:7])
    
    GPS_Info()
    return ''


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_view(get_home, route_name='home')
        config.add_route('apple', '/apple')
        config.add_view(apple, route_name='apple', renderer='json')
        config.add_route('orange', '/orange')
        config.add_view(orange, route_name='orange', renderer='json')
        config.add_route('banana', '/banana')
        config.add_view(banana, route_name='banana', renderer='json')
        config.add_route('gps', '/gps')
        config.add_view(gps, route_name='gps', renderer='json')
        config.add_route('run', '/run')
        config.add_view(run, route_name='run')
        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    print('Web server started on: http://0.0.0.0:6543')
    server.serve_forever()
