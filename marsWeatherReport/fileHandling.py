import json

def storeJsonDataToFile(data, filename): # this function stores json data into a specified file
    with open(filename + ".json", "w") as file:
        json.dump(data, file, indent=4) # dump method makes the json readable

def parseJsonDataFromFile(filename): # this function reads json data from a specified file
    with open(filename + ".json") as file:
        data = json.load(file)
        print(data["sol_keys"])