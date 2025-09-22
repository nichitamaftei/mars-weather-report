import os
import requests

def getWeatherFromMars(): # this function gets the data from NASA's restful api
    
    apiKey = os.getenv("NASA_API_KEY")
    if apiKey is None:
        raise ValueError("API_KEY is missing, please add your NASA API key as an enviroment variable")
    url = f"https://api.nasa.gov/insight_weather/?api_key={apiKey}&feedtype=json&ver=1.0"

    response = requests.get(url) # get the response object

    if response.status_code == 200: # if i get a successful response
        data = response.json() # json encode it
        return data   