#!/usr/bin/env python

__author__ = 'jsingh'

import requests
import turtle
import time


def main():
    # Part A
    r = requests.get('http://api.open-notify.org/astros.json')
    data = r.json()
    astros = r.json()['people']
    for i in range(len(astros)):
        print(astros[i]['name'] + ' is currently on board ' +
              astros[i]['craft'])
    print('')
    print('There is a total of ' + str(data['number']) +
          ' astronauts in space.')
    print('')

    # Part B
    r = requests.get('http://api.open-notify.org/iss-now.json')
    data = r.json()
    timestamp = data['timestamp']
    iss_position_lat = data['iss_position']['latitude']
    iss_position_long = data['iss_position']['longitude']
    print('Current Latidude: ' + iss_position_lat)
    print('Current Longitude: ' + iss_position_long)
    print('Timestamp: ' + str(timestamp))
    print('')

    # Part C
    screen = turtle.Screen()
    turtle.title('ISS Location')
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')

    screen.register_shape("iss.gif")
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.shape('iss.gif')
    pen.penup()
    pen.goto(float(iss_position_long), float(iss_position_lat))
    pen.stamp()
    pen.home()

    # Part D
    indy_lat = '39.7778261'
    indy_long = '-86.145737'
    payload = {'lat': indy_lat, 'lon': indy_long}
    r = requests.get('http://api.open-notify.org/iss-pass.json',
                     params=payload)
    data = r.json()['response']
    next_passover = time.ctime(data[0]['risetime'])

    pen.shape('circle')
    pen.color('yellow')
    pen.shapesize(.25)
    pen.goto(float(indy_long), float(indy_lat))
    pen.stamp()
    pen.write(next_passover)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
