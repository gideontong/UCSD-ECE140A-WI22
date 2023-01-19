#!/usr/bin/env python3
try:
    import RPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO
import time

trigPin = 23
echoPin = 24
MAX_DISTANCE = 220          # define maximum measuring distance, unit: cm
timeOut = MAX_DISTANCE*60   # calculate timeout w.r.t to maximum distance
buzzerPin = 6


def pulseIn(pin, level, timeOut):  # obtain pulse time of a pin under timeOut
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0
    pulseTime = (time.time() - t0)*1000000
    return pulseTime


def getSonar():            # get measurement of ultrasonic module, unit: cm
    GPIO.output(trigPin, GPIO.HIGH)   # make trigPin output 10us HIGH level
    time.sleep(0.00001)               # 10us
    GPIO.output(trigPin, GPIO.LOW)     # make trigPin output LOW level
    pingTime = pulseIn(echoPin, GPIO.HIGH, timeOut)  # read echoPin pulse time
    distance = pingTime*340.0/2.0/10000.0  # distance w/sound speed @ 340m/s
    return distance


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trigPin, GPIO.OUT)   # set trigPin to OUTPUT mode
    GPIO.setup(echoPin, GPIO.IN)    # set echoPin to INPUT mode
    GPIO.setup(buzzerPin, GPIO.OUT)


def Buzzer(distance):
    if distance > 0:
        GPIO.output(buzzerPin, GPIO.HIGH)
    else:
        GPIO.output(buzzerPin, GPIO.LOW)


def loop():
    while(True):
        distance = getSonar()  # get distance
        print("The distance is : %.2f cm" % (distance))
        Buzzer(distance)
        time.sleep(1)


if __name__ == '__main__':     # Program entrance
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press CTRL-C to end the program
        GPIO.cleanup()         # release GPIO resources
