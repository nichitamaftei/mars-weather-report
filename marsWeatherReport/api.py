import os
import requests

def getWeatherFromMars(): # this function gets the data from NASA's restful api
    
    apiKey = os.getenv("NASA_API_KEY")
    
    if apiKey is None:
        raise ValueError("API_KEY is missing, please add your NASA API key as an environment variable")
    
    url = f"https://api.nasa.gov/insight_weather/?api_key={apiKey}&feedtype=json&ver=1.0"

    try:
        response = requests.get(url, timeout=10) # get the response object with a max timeout of 10 sec
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise RuntimeError("NASA API request timed out")
    except requests.exceptions.ConnectionError:
        raise RuntimeError("Failed to connect to NASA API")
    except requests.exceptions.HTTPError as e:
        statusCode = e.response.status_code if e.response is not None else None
        # response.raise_for_status() triggers this
        if statusCode == 403:
            raise RuntimeError("Invalid API key or forbidden access") from e
        elif statusCode == 404:
            raise RuntimeError("NASA API endpoint not found") from e
        else:
            raise RuntimeError(f"HTTP error {statusCode}") from e
    except requests.exceptions.RequestException as e:
        # Catch-all for other errors
        raise RuntimeError(f"Unexpected error: {e}") from e
    
    
    if response.status_code == 200: # if i get a successful response
        data = response.json() # decodes the JSON data into a python dictionary
        
        filteredData = {}
        for key, value in data.items():
            if key.isdigit():
                filteredData[key] = value
            elif key == "sol_keys":
                filteredData[key] = value
    
        if filteredData != {}:
            return filteredData
        else:
            raise ValueError("No data found in the response")