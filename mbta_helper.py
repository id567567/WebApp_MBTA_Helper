import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)

MBTA_API_KEY = 'b27c9f30faed40b3b5f0bdd571efec4e'
MAPQUEST_API_KEY = 'rAMsEW4pLyT7KJ81DBWOObCMbA77JM0S'



# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

# location= input("Insert Your Location")
#
# url = "http://www.mapquestapi.com/geocoding/v1/address?key={}&location={}".format(MAPQUEST_API_KEY,location)
# print(get_json(url))


def get_lat_long(location):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """

    url = '{}?key={}&location={}'.format(MAPQUEST_BASE_URL, MAPQUEST_API_KEY, location)
    response = get_json(url)
    return response['results'][0]['locations'][0]['latLng']['lat'],  response['results'][0]['locations'][0]['latLng']['lng']

# print(get_lat_long(location))




def get_nearest_station(latitude, longitude):
    # latitude, longitude = get_lat_long()
    url = '{}?api_key={}&filter[latitude]={}&filter[longitude]={}&sort=distance'.format(MBTA_BASE_URL,MBTA_API_KEY,latitude,longitude)
    response=get_json(url)
    return response

print(get_nearest_station(42.355041,-71.066051))
#     """
#     Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
#     tuple for the nearest MBTA station to the given coordinates.
#     See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
#     formatting requirements for the 'GET /stops' API.
#     """
#     pass
#
#
# def find_stop_near(place_name):
#     """
#     Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
#     """
#     pass
#
#
# def main():
#     """
#     You can all the functions here
#     """
#     pass
#
#
# if __name__ == '__main__':
#     main()