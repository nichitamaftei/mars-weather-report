# importing the necessary libraries used for this script
import os
import requests
import json
from datetime import datetime 
import matplotlib.pyplot as plt

def getWeatherFromMars(): # this function gets the data from NASA's restful api
    
    apiKey = os.getenv("NASA_API_KEY")
    url = f"https://api.nasa.gov/insight_weather/?api_key={apiKey}&feedtype=json&ver=1.0"

    response = requests.get(url) # get the response object

    if response.status_code == 200: # if i get a successful response
        data = response.json() # json encode it
        return data    

def storeJsonDataToFile(data, filename): # this function stores json data into a specified file
    with open(filename + ".json", "w") as file:
        json.dump(data, file, indent=4) # dump method makes the json readable

def parseJsonDataFromFile(filename): # this function reads json data from a specified file
    with open(filename + ".json") as file:
        data = json.load(file)
        print(data["sol_keys"])
        print(json.dumps(data["675"], indent=4))
        
def day_with_suffix(day): # this function gets a day (e.g 3) and returns a string with its suffix
    if 11 <= day <= 13:
        return f"{day}th"
    last_digit = day % 10
    if last_digit == 1:
        return f"{day}st"
    elif last_digit == 2:
        return f"{day}nd"
    elif last_digit == 3:
        return f"{day}rd"
    else:
        return f"{day}th"
    
def plottingTemps(data, availableSols): # this function generates the graph
    yAvgTemps = []
    yMinTemps = []
    yMaxTemps = []
    
    for sol in availableSols: # for every sol (mars day) 
        yAvgTemps.append(data[sol]["AT"]["av"]) # adds the average temp to a list 
        
    for sol in availableSols:
        yMinTemps.append(data[sol]["AT"]["mn"]) # adds the lowest temp to a list
    
    for sol in availableSols:
        yMaxTemps.append(data[sol]["AT"]["mx"]) # adds the highest temp to a list

    # plots each line on the graph  
    plt.plot(availableSols, yAvgTemps, marker='o', label="Average", color="green")
    plt.plot(availableSols, yMinTemps, marker='o', label="Min", color="blue")
    plt.plot(availableSols, yMaxTemps, marker='o', label="Max", color="red")
    
    plt.legend()
    plt.xlabel("Sol")
    plt.ylabel("Temperature (°C)")
    plt.title("Mars Atmospheric Temperatures")
    plt.show()

def detailedSol(data, availableSols, solInput): # this function gives you specific details on the selected Sol (mars day)
    
    if solInput not in availableSols: # starts an infinite loop if the user's input isn't valid
        while True:
            solInput = str(input("Sol number not available or 'graph' typed incorrectly, please try again and select a Sol number from the available list OR type 'graph': "))
        
            if solInput == "graph":
                plottingTemps(data, availableSols)
            elif solInput not in availableSols:
                continue
            else: 
                break
    
    print(f"SOL {solInput} was chosen.")
    
    avgTemp = data[solInput]["AT"]["av"]
    print(f"Average temperature: {avgTemp}°C")
    
    lowestTemp = data[solInput]["AT"]["mn"]
    print(f"Lowest temperature recorded: {lowestTemp}°C")
    
    highestTemp = data[solInput]["AT"]["mx"]
    print(f"Highest temperature recorded: {highestTemp}°C")
        
def main(): # this function is the first to run
    print("Welcome to the Mars Weather Tracking application! \nBelow is a list of available Sol's containing data")
    
    data = getWeatherFromMars()
    availableSols = data["sol_keys"]

    for sol in availableSols: # spits out a list of all the available Sols
        dt = datetime.strptime(data[sol]['First_UTC'], "%Y-%m-%dT%H:%M:%SZ")
        formattedDate = f"{day_with_suffix(dt.day)} {dt.strftime('%B %Y')}"
        print(f"SOL {sol} ({formattedDate})")
    
    # asks the user what they want to do
    solInput = str(input("Please pick a Sol number from the list below to see the detailed weather stats OR type 'graph' to have a visualisation of these stats for all 7 Sols: "))
    
    if solInput == "graph": # if the user types "graph" then execute the plottingTemps() function with args
        plottingTemps(data, availableSols)
    else: # otherwise execute the detailedSol() function with args
        detailedSol(data, availableSols, solInput)
    
main() # executes the main() function