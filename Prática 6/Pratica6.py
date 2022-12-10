import json

from requests import get
from pprint import pprint

from time import sleep
from picamera import PiCamera

camera = PiCamera()

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

my_lat = -21.9900598
my_lon = -47.8902261

all_stations = get(stations).json()['items']

station_found = False

def find_closest():
    global station_found

    closest_station = all_stations[0]
    closest_distance = abs(my_lat - closest_station['weather_stn_lat']) + abs(
        my_lon - closest_station['weather_stn_long'])
    for station in all_stations:
        distance = abs(my_lat - station['weather_stn_lat']) + \
            abs(my_lon - station['weather_stn_long'])
        # Exclusão da estação que não está funcionando
        if distance < closest_distance and station['weather_stn_id'] != 19760370:
            closest_distance = distance
            closest_station = station
            station_found = True
    return closest_station['weather_stn_id']

closest_station = find_closest()

if station_found:
    weather += str(closest_station)
    weather = get(weather).json()['items']
    pprint(weather)

    for i in range(5):
        camera.start_preview()
        camera.annotate_text = "Temperatura: " + \
            str(closest_station['ambient_temp']) + "ºC" + \
            "Umidade: " + str(closest_station['humidity']) + "%"
        camera.annotate_text_size = 30
        sleep(5)
        camera.capture('Dados_11800910_11876933.jpg')
        camera.stop_preview()
